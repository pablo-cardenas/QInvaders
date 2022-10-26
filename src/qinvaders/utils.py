import numpy as np
import pygame
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
red = (255, 0, 0)
gris = (128, 128, 128)
orange = (255, 165, 0)
yellow = (255, 255, 0)


player_to_gates = {
    (1, 0, 0, 0, 0, 0, 0, 0): (0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0): (1, 0, 0),
    (1, 1, 0, 0, 0, 0, 0, 0): (2, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0): (0, 1, 0),
    (0, 0, 0, 1, 0, 0, 0, 0): (1, 1, 0),
    (0, 0, 1, 1, 0, 0, 0, 0): (2, 1, 0),
    (1, 0, 1, 0, 0, 0, 0, 0): (0, 2, 0),
    (0, 1, 0, 1, 0, 0, 0, 0): (1, 2, 0),
    (1, 1, 1, 1, 0, 0, 0, 0): (2, 2, 0),
    (0, 0, 0, 0, 1, 0, 0, 0): (0, 0, 1),
    (0, 0, 0, 0, 0, 1, 0, 0): (1, 0, 1),
    (0, 0, 0, 0, 1, 1, 0, 0): (2, 0, 1),
    (0, 0, 0, 0, 0, 0, 1, 0): (0, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 1): (1, 1, 1),
    (0, 0, 0, 0, 0, 0, 1, 1): (2, 1, 1),
    (0, 0, 0, 0, 1, 0, 1, 0): (0, 2, 1),
    (0, 0, 0, 0, 0, 1, 0, 1): (1, 2, 1),
    (0, 0, 0, 0, 1, 1, 1, 1): (2, 2, 1),
    (1, 0, 0, 0, 1, 0, 0, 0): (0, 0, 2),
    (0, 1, 0, 0, 0, 1, 0, 0): (1, 0, 2),
    (1, 1, 0, 0, 1, 1, 0, 0): (2, 0, 2),
    (0, 0, 1, 0, 0, 0, 1, 0): (0, 1, 2),
    (0, 0, 0, 1, 0, 0, 0, 1): (1, 1, 2),
    (0, 0, 1, 1, 0, 0, 1, 1): (2, 1, 2),
    (1, 0, 1, 0, 1, 0, 1, 0): (0, 2, 2),
    (0, 1, 0, 1, 0, 1, 0, 1): (1, 2, 2),
    (1, 1, 1, 1, 1, 1, 1, 1): (2, 2, 2),
}


class Input:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.players = [1] + 7 * [0]

        self._players_pressed = 8 * [0]
        self._gates_pressed = 6 * [0]

        self._gates = 3 * [0]

        self.font = pygame.font.Font(None, 30)
        self._title_height = height *0.2
        self._circuit_height = height *0.8
        self._title_surface = pygame.Surface((self.width, self._title_height))
        self._circuit_surface = pygame.Surface((self.width, self._circuit_height))
        self.surface = pygame.Surface((width, height))
        self.circuit = QuantumCircuit(3)
        self._is_quantum = False

    def switch(self):
        self._is_quantum = not self._is_quantum

    def poll_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.switch()
            return

        if self._is_quantum:
            self.poll_event_quantum(event)
        else:
            self.poll_event_classical(event)

    def update(self):
        if self._is_quantum:
            self.update_quantum()
        else:
            self.update_classical()

    def draw(self):
        title = self.font.render("Hard" if self._is_quantum else "Easy", True, purple)
        self._title_surface.fill(yellow)
        self._title_surface.blit(title, (0, 0))
        self.surface.blit(self._title_surface, (0,0))
        self.surface.blit(self._circuit_surface, (0,self._title_height))

    def poll_event_quantum(self, event):
        if event.type != pygame.KEYDOWN:
            return

        key_list = [
            pygame.K_q,
            pygame.K_w,
            pygame.K_a,
            pygame.K_s,
            pygame.K_z,
            pygame.K_x,
        ]
        key_dict = {key: i for i, key in enumerate(key_list)}
        event_gate = key_dict.get(event.key)

        if event_gate is None:
            return

        self._gates[event_gate // 2] ^= (event_gate % 2) + 1

    def poll_event_classical(self, event):
        if event.type not in (pygame.KEYDOWN, pygame.KEYUP):
            return

        key_list = [
            pygame.K_a,
            pygame.K_s,
            pygame.K_d,
            pygame.K_f,
            pygame.K_j,
            pygame.K_k,
            pygame.K_l,
            pygame.K_SEMICOLON,
        ]
        key_dict = {key: i for i, key in enumerate(key_list)}
        event_player = key_dict.get(event.key)

        if event_player is None:
            return

        if event.type == pygame.KEYDOWN:
            self._players_pressed[event_player] = 1
            if tuple(self._players_pressed) in player_to_gates:
                self.players[:] = self._players_pressed
        elif event.type == pygame.KEYUP:
            self._players_pressed[event_player] = 0

    def update_quantum(self):
        self.set_circuit()
        initial_state = Statevector.from_int(0, 2**3)
        self.players[:] = (np.abs(initial_state.evolve(self.circuit).data) ** 2).astype(bool).astype(int)

    def update_classical(self):
        self._gates[:] = player_to_gates[tuple(self.players)]
        self.set_circuit()

    def set_circuit(self):
        self.circuit = QuantumCircuit(3)
        self._circuit_surface.fill(white)
        width = self._circuit_surface.get_width()
        height = self._circuit_surface.get_height()
        for i in range(3):
            pygame.draw.line(
                self._circuit_surface,
                black,
                (0, height * (i + 0.5) / 3),
                (width, height * (i + 0.5) / 3),
            )
        for i, gate in enumerate(self._gates):
            if gate & 1:
                rect = [
                    (2*(gate&1) - 1) * width / 6 + height / 48,
                    i * height / 3 + height / 48,
                    width / 3 - 2 * height / 48,
                    height / 3 - 2 * height / 48,
                ]
                self.circuit.x(i)
                gate_name = "X"

                # Refactor because is the same code of the other if 
                pygame.draw.rect(self._circuit_surface, white, rect)
                pygame.draw.rect(self._circuit_surface, black, rect, 3)
                gate_name_surface = self.font.render(gate_name, True, black)
                self._circuit_surface.blit(gate_name_surface, (rect[0] + rect[2]/2-8, rect[1] + rect[3]/2-8))
            if gate & 2:
                rect = [
                    (2*(gate&2) - 1) * width / 6 + height / 48,
                    i * height / 3 + height / 48,
                    width / 3 - 2 * height / 48,
                    height / 3 - 2 * height / 48,
                ]
                self.circuit.h(i)
                gate_name = "H"

                # Refactor because is the same code of the other if 
                pygame.draw.rect(self._circuit_surface, white, rect)
                pygame.draw.rect(self._circuit_surface, black, rect, 3)
                gate_name_surface = self.font.render(gate_name, True, black)
                self._circuit_surface.blit(gate_name_surface, (rect[0] + rect[2]/2-8, rect[1] + rect[3]/2-8))
