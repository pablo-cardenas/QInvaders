# QInvaders

Quantum Space Invaders es una adaptación del clásico juego "Space Invaders" a una versión Cuántica.

El objetivo de este juego es mostrar que usando una estrategia cuántica se obtiene mejores puntajes que cuando se usa una estrategia clásica.

## Instalación

Use pip + git for installation 

```
$ pip install git+https://github.com/pablo-cardenas/QInvaders
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

  * Combinar las teclas A, S, D, F,  J, K, L, (; ó Ñ) para tener una superposición de estados.
  * SPACE: pausar el juego.
  * TAB: cambiar al modo difícil.

### Modo Difícil

En el modo difícil, uno debe diseñar el circuito cuántico  que genera la superposición de estados que uno quiere.

  * Usar las teclas Q, A, Z para poner una compuerta X.
  * Usar las teclas W, S, X para poner una compuerta H.
  * SPACE: pausar el juego.
  * TAB: cambiar al modo fácil.
