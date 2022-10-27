# QInvaders

Quantum Space Invaders es una adaptación del clásico juego "Space Invaders" a una versión Cuántica.

El objetivo de este juego es mostrar que usando una estrategia cuántica se obtiene mejores puntajes que cuando se usa una estrategia clásica.

## Instalación

Use pip + git for installation 

```
$ pip install --force-reinstall git+https://github.com/pablo-cardenas/QInvaders@main
```

Para correr QInvaders, simplemente ejecutar `qinvaders`  en la terminal

```
$ qinvaders
```

## Cómo jugar

Se debe evitar la invasión destruyendo a los invasores.
Para ello se tiene un cañón **quántico**  que lanza misiles **quánticos**.

El cañón puede estar en un estado de superposición, es decir, puede estar en *varios lugares a la vez*.
Durante todo el juego, el cañón estará lanzando misiles.
Estos misiles estarán en un estado de superposición mientras no lo hayan visto los invasores, es decir, mientras no se haya *medido*.
Al momento de hacer la medición, los misiles colapsan en un único estado y podrá impactar con las naves.

El objetivo es evitar la invasión con la **mínima cantidad de cambios de estados** del cañón por minuto.

Este juego tiene dos modos: modo FÁCIL y modo DIFÍCIL. La tecla TAB sirve para cambiar entre el modo fácil y el modo difícil.

### Modo Fácil

En el modo fácil, uno debe escoger los estados que quiere superponer.

  * Combinar las teclas A, S, D, F, H, J, K, L para tener una superposición de estados.
  * SPACE: pausar el juego.
  * TAB: cambiar al modo difícil.

### Modo Difícil

En el modo difícil, uno debe diseñar el circuito cuántico  que genera la superposición de estados que uno quiere.

  * Usar las teclas Q, A, Z para poner una compuerta X.
  * Usar las teclas W, S, X para poner una compuerta H.
  * SPACE: pausar el juego.
  * TAB: cambiar al modo fácil.


## Ventaja Cuántica

Este juego muestra que es más ventajoso tener una estrategia cuántica que tener una estrategia clásica.

### Estrategia Clásica

La estrategia clásica es usar el cañón sin superposición, es decir en un sólo estado a la vez (determinístico).
Entonces, los misiles serán lanzados en una sóla posición.
Sin embargo, se tendrá que cambiar la posición del cañón para poder impactar a todos los invasores.

Hay momentos en que vienen muchos invasores a la vez.
Supongamos que hay 4 invasores viniendo a la vez y que estamos usando la estrategia clásica.
Entonces, se tendría que hacer 4 movimientos para atacar a esos 4 invasores.
Sin embargo, en la estrategia cuántica, sólo se necesita un movimiento.

### Estrategia Cuántica

La estrategia cuántica permite usar el cañón en un estado de superposición, es decir, que puede estar en varios lugares a la vez.

En los momentos que vengan varios invasores a la vez.
Se puede atacar a todos los invasores usando sólamente un estado superpuesto.

Nota: La estrategia de usar el estado totalmente entrelazado siempre
`(|000>+|001>+|010>+|011>+|100>+|101>+|110>+|111>)/sqrt(8)` **no funciaría**, 
ya que sería enviar misiles superpuestos en todas las posiciones a la vez.
Al momento de colapsar escogería aleatoriamente cualquier posición y
varios de esos misiles **no impactarían** con ningún invasor.

### Comparación: Cuántica > Clásica

Se observa que usando la estrategia clásica se consigue una eficienca de 2000 y usando la estrategia cuántica se puede superar los 5000

