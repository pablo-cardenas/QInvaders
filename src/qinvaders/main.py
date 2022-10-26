import random

import pygame

from .utils import Input
from .utils import player_to_gates

pygame.init()

def main():
    # constantes
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    purple = (128, 0, 128)
    red = (255, 0, 0)
    gris = (128, 128, 128)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)

    space_width = 480
    space_height = 720
    barrier_y = 240
    screen = pygame.display.set_mode([space_width + 120, space_height])
    space_surface = pygame.Surface([space_width, space_height])

    pygame.display.set_caption("Infinite QRunner")
    background = black
    fps = 60
    font = pygame.font.Font(None, 60)
    font_state = pygame.font.Font(None, 20)
    clock = pygame.time.Clock()
    running = True
    paused = False

    input = Input(120, 120)

    speed_invader = 1
    speed_bullet = 8

    freq_change = 300
    prop_change = 0.2
    freq_invaders = 10
    freq_bullet = 10

    bullets = [(0, (0,), 0, 0)]  # (-step, possible, pos_collapsed, is_collapsed)
    bullets_rects = []

    invaders = [(0, 0)]
    invaders_rects = []
    invaders_positions = {0}

    cannons_positions = {0}


    cannon_size = 20
    invader_width = 20
    invader_height = 5
    bullet_height = 5
    bullet_width = 2

    prev_cannons = {0}
    changes = [0]

    step = 0
    while running:
        if not paused:
            step += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    break

            input.poll_event(event)

        input.update()
        cannons_positions = {i for i, valid in enumerate(input.players) if valid}

        if not paused:
            if cannons_positions != prev_cannons:
                prev_cannons = cannons_positions
                if step - changes[-1] > 10:
                    changes.append(step)

            if step % freq_change == 0:
                invaders_positions = {
                    i
                    for i, valid in enumerate(
                        random.choice(list(player_to_gates.keys()))
                    )
                    if valid
                }

            if (
                step % (freq_invaders * len(invaders_positions)) == 0
                and step % freq_change > prop_change * freq_change
            ):
                for i in invaders_positions:
                    invaders.append((step, i))

            if step % freq_bullet == 0:
                possible = tuple(cannons_positions)
                collapsed = random.choice(list(cannons_positions))
                bullets.append((step, possible, collapsed, 0))

            # Collision bullet invasor
            for k in range(8):
                try:
                    i_bullet = next(
                        i for i, (_, _, pos, _) in enumerate(bullets) if pos == k
                    )
                    i_invader = next(
                        i for i, (_, pos) in enumerate(invaders) if pos == k
                    )
                except StopIteration:
                    continue

                invader_step = invaders[i_invader][0]
                bullet_step = bullets[i_bullet][0]
                invader_pos_y = step - invader_step
                bullet_pos_y = space_height - speed_bullet * (step - bullet_step)
                if invader_pos_y > bullet_pos_y:
                    del bullets[i_bullet]
                    del invaders[i_invader]

            # Game Over
            invaders_max_y = step - (invaders[0][0])
            if invaders_max_y >= space_height:
                running = False
                break

            # Bullet Collapsed
            for i, (
                bullet_step,
                possible_pos,
                pos_collapsed,
                is_collapsed,
            ) in enumerate(bullets):
                bullet_pos_y = space_height - speed_bullet * (step - bullet_step)
                if bullet_pos_y < invaders_max_y:
                    bullets[i] = (bullet_step, possible_pos, pos_collapsed, 1)

            # Remove bullets
            bullet_min_y = space_height - speed_bullet * (step - bullets[0][0])
            while bullet_min_y < barrier_y:
                bullets.pop(0)
                bullet_min_y = space_height - (step - bullets[-1][0])

        ########
        # Draw #
        ########
        input.draw()
        screen.fill(background)
        space_surface.fill(background)

        # Draw score
        num_changes = len(changes)
        changes_lastminute = sum(1 for s in changes if s > step - 60 * fps)
        score = changes_lastminute / min(1, (step / 60 / fps) ** 2)
        score_text = font.render(f"{score:0.1f}", True, white)
        changes_text = font.render(str(num_changes), True, white)

        # Draw lines
        pygame.draw.line(
            space_surface,
            gris,
            (0, barrier_y),
            (space_width, barrier_y),
        )
        for i in range(9):
            pygame.draw.line(
                space_surface,
                gris,
                (space_width * i / 8, 0),
                (space_width * i / 8, space_height),
            )

        # Invaders
        for invader_step, pos in invaders:
            invaders_rects.append(
                pygame.draw.rect(
                    space_surface,
                    orange,
                    [
                        (pos + 0.5) * space_width / 8 - invader_width / 2,
                        step - invader_step,
                        invader_width,
                        invader_height,
                    ],
                )
            )

        # Bullet
        for bullet_step, possible_pos, pos_collapsed, is_collapsed in bullets:
            bullet_pos_y = space_height - speed_bullet * (step - bullet_step)
            if is_collapsed:
                bullets_rects.append(
                    pygame.draw.rect(
                        space_surface,
                        orange,
                        [
                            (pos_collapsed + 0.5) * space_width / 8
                            - bullet_width / 2,
                            bullet_pos_y,
                            bullet_width,
                            bullet_height,
                        ],
                    )
                )
            else:
                for pos in possible_pos:
                    bullets_rects.append(
                        pygame.draw.rect(
                            space_surface,
                            green,
                            [
                                (pos + 0.5) * space_width / 8 - bullet_width / 2,
                                bullet_pos_y,
                                bullet_width,
                                bullet_height,
                            ],
                        )
                    )

        # Cannon
        for pos in cannons_positions:
            player = pygame.draw.rect(
                space_surface,
                white,
                [
                    (pos + 0.5) * space_width / 8 - cannon_size / 2,
                    space_height - cannon_size,
                    cannon_size,
                    cannon_size,
                ],
            )

        for pos in range(8):
            state_text = font_state.render(f"|{pos:03b}>", True, white)
            space_surface.blit(
                state_text,
                (
                    (pos + 0.5) * space_width / 8 - state_text.get_width() / 2,
                    space_height - 40,
                ),
            )

        screen.blit(changes_text, (0, 0))
        screen.blit(score_text, (0, 80))
        screen.blit(input.surface, (0, space_height - 120))
        screen.blit(space_surface, (120, 0))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

