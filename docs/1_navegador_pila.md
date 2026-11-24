# Navegador web con pilas

## Introducción

En este proyecto hicimos un navegador web que simula los botones Back y Forward, los que sirven para regresar a la página anterior y para volver a avanzar. Son botones que usamos todos los días, pero detrás de ellos hay una estructura de datos muy sencilla: la pila. Con dos pilas y una variable para la página actual se puede guardar todo el historial y moverse hacia atrás y hacia adelante sin perder ninguna página.

## La pila

Una pila funciona como una pila de platos: el último que se pone es el primero que se quita. A esto se le llama LIFO, que significa último en entrar, primero en salir. Solo se puede trabajar con el elemento de hasta arriba, que se llama tope.

Es una de las estructuras más antiguas de la computación. Alan Turing ya hablaba de ella en 1946 y en 1955 Klaus Samelson y Friedrich L. Bauer la propusieron formalmente y la patentaron en 1957. Hoy está en todos lados, por ejemplo en el botón de deshacer de cualquier programa, en las llamadas a funciones de los lenguajes de programación y en el historial del navegador.

## Cómo funciona el código

La clase `Pila` guarda sus elementos en una lista de Python, y el final de la lista es el tope. Se hace así porque agregar y quitar al final de una lista es inmediato.

| Método | Qué hace | Cómo lo hace | Complejidad |
|--------|----------|--------------|-------------|
| `apilar(e)` | Pone un elemento en el tope | `self.elementos.append(e)` | O(1) |
| `desapilar()` | Quita y regresa el tope | `self.elementos.pop()` | O(1) |
| `ver_tope()` | Regresa el tope sin quitarlo | `self.elementos[-1]` | O(1) |
| `esta_vacia()` | Dice si la pila no tiene elementos | `len(self.elementos) == 0` | O(1) |
| `vaciar()` | Borra todos los elementos | `self.elementos = []` | O(1) |

La clase `NavegadorWeb` usa dos pilas y una variable:

- `pila_atras` guarda las páginas que se visitaron antes de la actual.
- `pila_adelante` guarda las páginas de las que se regresó con Back, para poder volver con Forward.
- `pagina_actual` es la página que se está viendo en ese momento.

Cada botón mueve las páginas de una pila a otra:

| Acción | Qué pasa |
|--------|----------|
| Visitar una página | La página actual se guarda en la pila de atrás, la pila de adelante se vacía y la nueva página pasa a ser la actual |
| Back | La página actual se guarda en la pila de adelante y se saca el tope de la pila de atrás |
| Forward | La página actual se guarda en la pila de atrás y se saca el tope de la pila de adelante |

## Ejemplo paso a paso

| Paso | Página actual | Pila atrás | Pila adelante |
|------|---------------|------------|---------------|
| Visitar google.com | google.com | vacía | vacía |
| Visitar github.com | github.com | google.com | vacía |
| Visitar youtube.com | youtube.com | google.com, github.com | vacía |
| Back | github.com | google.com | youtube.com |
| Back | google.com | vacía | youtube.com, github.com |
| Forward | github.com | google.com | youtube.com |
| Visitar anahuac.mx | anahuac.mx | google.com, github.com | se vacía |

En las pilas el último elemento escrito es el tope.

## La ventana del proyecto

La ventana tiene los botones Back y Forward, un cuadro para escribir la dirección y el botón Visitar, que también funciona al presionar Enter. Abajo se dibujan las dos pilas como cajas, una encima de otra, y el tope aparece en amarillo con la palabra TOPE. Cuando una pila está vacía su botón se desactiva para que no se pueda presionar.

## Detalles a tener en cuenta

- Los métodos `desapilar` y `ver_tope` no revisan si la pila está vacía, pero nunca falla porque el navegador siempre pregunta antes con `esta_vacia`, y en la ventana además se desactivan los botones.
- La pila de adelante se vacía cada vez que se visita una página nueva, porque a partir de ahí el historial toma otro camino y las páginas que seguían ya no tienen sentido. Así funcionan los navegadores reales.
- El historial no tiene límite. Para este proyecto no es necesario, pero un navegador real guarda solo cierto número de páginas.

## Preguntas que nos pueden hacer en la exposición

- **¿Por qué el tope es el final de la lista y no el inicio?** Porque agregar y quitar al final de una lista es O(1), mientras que hacerlo al inicio es O(n) porque se tienen que recorrer todos los elementos.
- **¿Qué pasa si se presiona Back sin historial?** El método revisa primero si la pila de atrás está vacía y solo muestra un mensaje, el programa no truena.
- **¿Por qué se usan dos pilas?** Una guarda el camino hacia atrás y la otra el camino hacia adelante, y cada botón pasa la página actual de una a la otra.

## Conclusión

La pila es una estructura muy simple, pero resuelve el historial del navegador de forma muy limpia. Con dos pilas se puede ir y regresar sin perder ninguna página y todas las operaciones son inmediatas. Lo más importante del proyecto es entender por qué la última página que se visitó es la primera a la que se regresa, que es justamente la regla de la pila.

## Fuentes

- Python Software Foundation. *Using Lists as Stacks*. https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
- Samelson, K. y Bauer, F. L. Sequential formula translation. *Communications of the ACM*, vol. 3, núm. 2, pp. 76–83, 1960.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*, 4.ª edición, capítulo 10. MIT Press, 2022.
