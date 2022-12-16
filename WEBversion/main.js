const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width = 1024
canvas.height = 600

let start_drivers = false
var cannons_positions = [1, 0, 0, 0, 0, 0, 0, 0]

const player = new Player()
let projectiles = []
let frames = 0;
let grids = []
let randomInterval = Math.floor(Math.random() * 50 + 50)
let spawnBuffer = 120

var pause = false
let score = 0

function animate(){
    if(pause) return;

    requestAnimationFrame(animate)
    
    c.fillStyle = 'black'
    c.fillRect(0,0,canvas.width,canvas.height)

    c.strokeStyle = '#ff0000';
    for (let i=0; i<8;i++){
        c.beginPath();
        c.moveTo(224 + 100*i ,0);
        c.lineTo(224 + 100*i ,576);
        c.stroke();
    }    
    
    // nave
    player.update()
    
    if (frames % 12 === 0 ) {
        player.shoot(projectiles)
      }

    for (let i = projectiles.length - 1; i >= 0; i--) {
        const projectile = projectiles[i]
        projectile.update()
    } 

    // invasores
    grids.forEach((grid,gridIndex) => {
        grid.update()

        for (let i = grid.invaders.length - 1; i >= 0; i--) {
          const invader = grid.invaders[i]
          invader.update({ velocity: grid.velocity })

          // disparando a los invasores
          if (invader.position !== undefined){

            projectiles.forEach((projectile, j) => {
            
              if (
                projectile.position.y - projectile.radius <=
                  invader.position.y + invader.height &&
                projectile.position.x + projectile.radius >= invader.position.x &&
                projectile.position.x - projectile.radius <=
                  invader.position.x + invader.width &&
                projectile.position.y + projectile.radius >= invader.position.y
              ) {
                setTimeout(() => {
                  const invaderFound = grid.invaders.find(
                    (invader2) => invader2 === invader
                  )
                  const projectileFound = projectiles.find(
                    (projectile2) => projectile2 === projectile
                  )
      
                  // removiendo proyectiles e invasores
                  if (invaderFound && projectileFound) {
                    score += 100
                    console.log(score)
  
                    grid.invaders.splice(i, 1)
                    projectiles.splice(j, 1)
      
                    if (grid.invaders.length > 0) {
                      const firstInvader = grid.invaders[0]
                      const lastInvader = grid.invaders[grid.invaders.length - 1]
      
                      grid.width =
                        lastInvader.position.x -
                        firstInvader.position.x +
                        lastInvader.width
                      grid.position.x = firstInvader.position.x
                    } else {
                      grids.splice(gridIndex, 1)
                    }
                  }
                }, 0)
              }
              
            })
          }
        } 
      })

    if (frames % randomInterval === 0) {
        grids.push(new Grid())
        randomInterval = Math.floor(Math.random() * 80 + spawnBuffer)
        frames = 0
      }    
    frames ++    
}

function controllers(){
  if (start_drivers){
    window.addEventListener("keydown", function (e) {
        console.log(e.keyCode)
        // si es la tecla 'p'
        if(e.keyCode == 80){
            switchTF();
        }
        if(e.keyCode == 32){
            pause = !pause
            if(!pause){
                animate()
            }
        }
  
        if (quantum_activate){
            poll_event_quantum(e.keyCode)
            console.log('activo')
        }
        else{
            poll_event_classical(e.keyCode);
        }
    });
  }
}

document.querySelector('#start').addEventListener('click',()=>{
  document.querySelector('.window2').style.display = 'none'
  document.querySelector('.window1').style.display = 'none'
  start_drivers = true
  controllers();
  animate();
})

document.querySelector('#instructions').addEventListener('click',()=>{
  document.querySelector('.window1').style.display = 'none'
})

document.querySelector('#close__instructions').addEventListener('click',()=>{
  document.querySelector('.window1').style.display = 'block'
})
