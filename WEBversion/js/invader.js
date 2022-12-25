class Invader {
  constructor({ position }) {
    this.velocity = {
      x: 0,
      y: 0
    }

    const image = new Image()
    image.src = './img/invader.png'
    image.onload = () => {
      const scale = 0.9 
      this.image = image
      this.width = image.width * scale
      this.height = image.height * scale
      this.position = {
        x: position.x,
        y: position.y
      }
    }
  }

  draw() {
    c.drawImage(
      this.image,
      this.position.x,
      this.position.y,
      this.width,
      this.height
    )
  }

  update({ velocity }) {
    if (this.image) {
      this.draw()
      this.position.x += velocity.x
      this.position.y += velocity.y
    }
  }
}



class Grid {
  constructor() {
    this.position = {
      x: 0,
      y: 0
    }

    this.velocity = {
      x: 0,
      y: 0
    }

    this.invaders = []

    const matrix_init = generateMatrix();
    const rows = Math.floor(Math.random() * 4 + 3)

    for (let x = 0; x < matrix_init.length; x++) {
      if (matrix_init[x] == 1){
        for (let y = 0; y < rows; y++) {
          this.invaders.push(
            new Invader({
              position: {
                x: x * 100 + 274 - 15,
                y: y * 25 - 200
              }
            })
            )
          }
        }
    }
  }

  update() {
    this.position.y += this.velocity.y
    this.velocity.y = 1
  }
}
