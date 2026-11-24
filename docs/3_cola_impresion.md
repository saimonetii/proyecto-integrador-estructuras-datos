# Cola de impresión

## Introducción

En este proyecto simulamos una impresora compartida por cinco computadoras, de la PC1 a la PC5. Cuando varias personas mandan a imprimir al mismo tiempo, la impresora no las puede atender a todas a la vez, así que los trabajos se forman en una cola y se imprimen en el orden en que llegaron. La cola tiene una capacidad máxima de seis trabajos, igual que una impresora real que tiene memoria limitada.

## La cola

Una cola funciona como la fila del banco o de las tortillas: el primero que llega es el primero que atienden. A esto se le llama FIFO, que significa primero en entrar, primero en salir. Los elementos nuevos se agregan al final y se atienden por el frente.

El estudio formal de las colas empezó con el ingeniero danés A. K. Erlang, que en 1909 analizó cuántas llamadas podía atender una central telefónica. En computación las colas están en todo lo que se atiende por turnos, como la cola de impresión del sistema operativo, los mensajes que recibe un servidor o los procesos que esperan al procesador.

## Cómo funciona el código

El programa tiene dos constantes:

| Constante | Valor | Para qué sirve |
|-----------|-------|----------------|
| `CAPACIDAD_MAXIMA` | 6 | Cuántos trabajos caben en la cola |
| `COMPUTADORAS` | PC1, PC2, PC3, PC4, PC5 | Las computadoras que pueden mandar trabajos |

La clase `ColaImpresion` guarda los trabajos en una lista:

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `esta_vacia()` | Dice si no hay trabajos | O(1) |
| `esta_llena()` | Dice si ya se llegó a la capacidad | O(1) |
| `encolar(e)` | Si hay espacio agrega el trabajo al final y regresa True, si está llena regresa False | O(1) |
| `desencolar()` | Quita y regresa el trabajo del frente, y si está vacía regresa None | O(n) |

El menú de consola tiene cuatro opciones: agregar un trabajo de una PC elegida al azar con `random.choice`, agregar un trabajo escribiendo el nombre de la PC, imprimir el documento que está al frente y mostrar cómo va la cola.

## Ejemplo paso a paso

| Acción | Cola del frente al final | Capacidad usada |
|--------|--------------------------|-----------------|
| Agregar PC3 | PC3 | 1 de 6 |
| Agregar PC1 | PC3, PC1 | 2 de 6 |
| Agregar PC5 | PC3, PC1, PC5 | 3 de 6 |
| Imprimir | PC1, PC5 | 2 de 6 |

Al imprimir sale la PC3, porque fue la primera que llegó.

## La ventana del proyecto

La ventana tiene un botón para agregar un trabajo de una PC al azar, una lista para elegir la PC y otro botón para agregar ese trabajo, y el botón Imprimir documento. Se dibujan los seis lugares de la cola con el frente a la izquierda y el final a la derecha, y cada PC tiene su propio color. Abajo hay un historial de impresión que muestra en qué orden salieron los documentos, lo que demuestra que se respeta el orden de llegada.

## Detalles a tener en cuenta

- Para sacar el trabajo del frente se usa `pop(0)`, que tiene que recorrer todos los demás elementos un lugar. Con seis trabajos no se nota, pero con miles convendría usar `collections.deque`, que lo hace de forma inmediata.
- Cuando la cola está llena, los trabajos nuevos no se agregan y el programa avisa que está llena. Así se comporta una impresora real cuando su memoria se llena.
- Si se escribe el nombre de la PC en minúsculas también funciona, porque el programa lo convierte a mayúsculas.

## Preguntas que nos pueden hacer en la exposición

- **¿Qué diferencia hay con la pila del proyecto 1?** En la pila sale el último que entró y en la cola sale el primero que entró.
- **¿Qué pasa si la cola está llena?** El método `encolar` regresa False y no agrega nada, y el programa muestra que la cola está llena.
- **¿Por qué tiene capacidad limitada?** Para parecerse a una impresora real, que solo puede guardar cierta cantidad de trabajos en espera.

## Conclusión

La cola es la estructura correcta para todo lo que se debe atender por turnos y de forma justa, porque el primero que llega es el primero que sale. La capacidad limitada hace que el proyecto se parezca más a la realidad, y el dibujo de la ventana permite ver cómo los trabajos avanzan del final hacia el frente hasta que se imprimen.

## Fuentes

- Python Software Foundation. *Using Lists as Queues*. https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
- Python Software Foundation. *collections.deque*. https://docs.python.org/3/library/collections.html#collections.deque
- Erlang, A. K. The theory of probabilities and telephone conversations. *Nyt Tidsskrift for Matematik B*, vol. 20, pp. 33–39, 1909.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*, 4.ª edición, capítulo 10. MIT Press, 2022.
