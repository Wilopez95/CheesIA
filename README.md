# Ajedres utilizando 
## Caracteristicas
Este pequeño programa de ajedres utiliza un algoritmo de **backtrackking** en conjunto con la poda **alfa-beta** para determinar el mejor movimineto en un turno dado

### Formato de movimientobrs
Para realizar un movimiento utilizando la consola debes:<>
Dar la **posicion orignal** separado por **-** o **:** seguido por la **posicion final**<br>
Por ejemplo:
~~~
F7-F6
D1-B3
E7-E5
B1-C3
~~~

### Formato del log
Para representar los movimientos de la partida se genera un log. El cual tiene el siguiente formato:

| Ficha Inicial   |      Posicion      | Come? | Posicion Final |
|----------|:-------------:|:------:|------:|
| R |  D2 | x | E3 |
| p |  F5   |-|   F4 |
| p | E4 |-|    E3 |
| N | G1 |-|    F3 |

Una letra representa la **pieza que se movio**.<br>
**Posicion inicial**.<br>
X si al hacer este movimiento se **come una pieza**.<br>
**Posicion final**.<br>

*Cabe destacar que para poder reconstruir una partida solo es necesario el estado inicial de la partida y las pocisiones en las que se realizan los movimientos*

## Autores
Wilson Lopez Rubi
Carlos Gomez Soza
Juan Jose Solano