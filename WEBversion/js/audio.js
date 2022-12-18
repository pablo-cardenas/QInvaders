Howler.volume(0.5)
const audio = {
  backgroundMusic: new Howl({
    src: './audio/backgroundMusic.wav',
    loop: true
  }),
  explode: new Howl({
    src: './audio/explode.wav',
    volume: 0.3
  }),
  gameOver: new Howl({
    src: './audio/gameOver.mp3'
  }),
  select: new Howl({
    src: './audio/select.mp3',
    volume: 0.8
  }),
  start: new Howl({
    src: './audio/start.mp3'
  })
}
