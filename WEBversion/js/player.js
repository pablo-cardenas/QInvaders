class Player{
    constructor(){

        const image = new Image()
        image.src = "./img/spaceship.png"
        image.onload = () =>{
            const scala = 0.15
            this.image = image
            this.width = image.width*scala
            this.height = image.height*scala
            this.position = {
                x: 274 - this.width/2,
                y: canvas.height - this.height -25 
            }
        }
    }
    draw(){
        for (let i = 0; i < cannons_positions.length; i += 1) {
            if (cannons_positions[i] == 1){
                if (this.image)
                c.drawImage(
                    this.image,
                    this.position.x + 100*i,
                    this.position.y,
                    this.width,
                    this.height
                )}}
    }
    update(){
        this.draw()
    }

    shoot(projectiles) {
        for (let i = 0; i < cannons_positions.length; i++) {

            if (cannons_positions[i] == 1){
                projectiles.push(
                    new Projectile({
                      position: {
                        x:274 + i*100,
                        y: canvas.height - this.height -30
                      },
                      velocity: {
                        x: 0,
                        y: -6
                      }
                    })
                  )}
            }
        }
        
}