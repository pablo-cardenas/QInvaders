const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width = 1024
canvas.height = 600

let cannons_positions, player, projectiles;
let frames, grids, randomInterval, spawnBuffer,eficiencia;
let pause, score, changeStep, end_game, modo_text;


function initCanvas(){
  
  cannons_positions = [1, 0, 0, 0, 0, 0, 0, 0]
  
  player = new Player()
  projectiles = []
  frames = 0;
  grids = []
  randomInterval = Math.floor(Math.random() * 50 + 50)
  spawnBuffer = 120
  
  pause = false
  score = 0
  changeStep = 1
  end_game = false
  modo_text = "Clásico"
}

function endGame(){

  end_game = true

  setTimeout(() => {
      audio.gameOver.play()
    }, 0)

    setTimeout(() => {
      document.querySelector('.window3').style.display = 'block'
    }, 1000)
    document.querySelector('#eficienciaNC').innerHTML = Math.floor(eficiencia) 
}


function animate(){

  if (end_game) return;

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

    c.font = "15px serif"
    c.fillStyle = "white"
    c.fillText("|000⟩",274-15,590)   
    c.fillText("|001⟩",374-15,590)   
    c.fillText("|010⟩",474-15,590)   
    c.fillText("|011⟩",574-15,590)   
    c.fillText("|100⟩",674-15,590)   
    c.fillText("|101⟩",774-15,590)   
    c.fillText("|110⟩",874-15,590)   
    c.fillText("|111⟩",974-15,590)
    
    c.font = "20px serif"
    c.fillText(`Score: ${score}`,50,50)
    c.fillText(`Eficiencia: ${Math.floor(eficiencia)}`,50,80)
    c.fillText(`Modo ${modo_text}`,50,200)

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
    grids.forEach((grid) => {
        grid.update()

        for (let i = grid.invaders.length - 1; i >= 0; i--) {
          const invader = grid.invaders[i]
          invader.update({ velocity: grid.velocity })

          if (invader.position !== undefined){
            
            // disparando a los invasores
            projectiles.forEach((projectile, j) => {

              // desaparecer misiles sin se encuentran fuera del lienzo
              if (projectile.position.y < 10){
                projectiles.splice(j, 1)
              }
            
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
                    score += 1
                    audio.explode.play()
                    grid.invaders.splice(i, 1)
                    projectiles.splice(j, 1)
                  }
                }, 0)
              }
              
            })

          // llegada invasores a la meta
          if (canvas.height - invader.position.y < 50){
            endGame();
          }
          }

        } 
      })

    if (frames % randomInterval === 0) {
        grids.push(new Grid())
        randomInterval = Math.floor(Math.random() * 80 + spawnBuffer)
        frames = 0
      }   
      
    // eficiencia = (Resultado alcanzado / Coste total) x Tiempo invertido
    eficiencia = (score / changeStep) * window.performance.now() * 0.001
    frames ++   
}

function controllers(){
    addEventListener("keydown", function (e) {

        if(e.keyCode == 80){
            audio.select.play()
            switchTF();
        }
        if(e.keyCode == 32){
          pause = !pause
          animate()
          console.log(pause)
        }
  
        if (quantum_activate){
            poll_event_quantum(e.keyCode)
            modo_text = "Cuántico"
            changeStep +=1
        }
        else{
            poll_event_classical(e.keyCode);
            modo_text = "Clásico"
            changeStep +=1
        }
    });
}

document.querySelector('#start').addEventListener('click',()=>{
  audio.backgroundMusic.play()
  audio.start.play()
  document.querySelector('.window3').style.display = 'none'
  document.querySelector('.window2').style.display = 'none'
  document.querySelector('.window1').style.display = 'none'
  initCanvas();
  controllers()
  animate();
})

document.querySelector('#restart').addEventListener('click',()=>{
  audio.start.play()
  document.querySelector('.window2').style.display = 'none'
  document.querySelector('.window1').style.display = 'none'
  document.querySelector('.window3').style.display = 'none'
  initCanvas();
  animate();
})

document.querySelector('#instructions').addEventListener('click',()=>{
  audio.select.play()
  document.querySelector('.window1').style.display = 'none'
})

document.querySelector('#close__instructions').addEventListener('click',()=>{
  audio.select.play()
  document.querySelector('.window1').style.display = 'block'
})
