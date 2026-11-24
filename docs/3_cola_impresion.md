# Proyecto 3: Cola de impresión

[← Volver al README](../README.md) · Código: [`proyectos/p3_cola_impresion.py`](../proyectos/p3_cola_impresion.py) · Ventana: [`interfaz/ventana_cola.py`](../interfaz/ventana_cola.py)

## Introducción

Hablaremos del tercer proyecto: una impresora compartida por cinco computadoras (PC1 a PC5). Cuando varias personas mandan a imprimir al mismo tiempo, la impresora no puede atenderlas a todas a la vez, así que los trabajos se forman en una **cola** y se imprimen en el orden en que llegaron. La cola tiene una **capacidad máxima de 6** trabajos.

## Origen

Las colas vienen de la vida diaria (la fila del banco, de las tortillas o del súper) y su estudio formal empezó con la **teoría de colas** del ingeniero danés A. K. Erlang, que en 1909 analizó cuántas llamadas podía atender una central telefónica. En computación la cola se usa en todo lo que debe atenderse por turnos: la cola de impresión del sistema operativo, los mensajes de un servidor o los procesos que esperan al procesador.

## Funcionamiento

Una cola funciona como una fila: el **primero en entrar es el primero en salir** (FIFO, *First In, First Out*). Se agrega por el **final** y se atiende por el **frente**.

### Constantes

| Constante | Valor | Para qué sirve |
|-----------|-------|----------------|
| `CAPACIDAD_MAXIMA` | 6 | Cuántos trabajos caben en la cola |
| `COMPUTADORAS` | PC1, PC2, PC3, PC4, PC5 | Las computadoras que pueden mandar trabajos |

### Clase `ColaImpresion`

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `esta_vacia()` | Dice si no hay trabajos | O(1) |
| `esta_llena()` | Dice si ya hay 6 trabajos | O(1) |
| `encolar(e)` | Si hay espacio, agrega al final y regresa `True`; si está llena regresa `False` | O(1) |
| `desencolar()` | Quita y regresa el trabajo del frente (`pop(0)`); si está vacía regresa `None` | O(n) |

### Ejemplo

| Acción | Cola (frente → final) | Capacidad |
|--------|----------------------|-----------|
| Agregar PC3 | PC3 | 1/6 |
| Agregar PC1 | PC3 → PC1 | 2/6 |
| Agregar PC5 | PC3 → PC1 → PC5 | 3/6 |
| Imprimir | PC1 → PC5 (se imprimió **PC3**, el primero) | 2/6 |

### En la interfaz

Hay botones para agregar un trabajo de una PC aleatoria (`random.choice`) o de la PC elegida en una lista, y el botón **Imprimir documento**. Se dibujan los 6 lugares de la cola con el **FRENTE** a la izquierda y el **FINAL** a la derecha, cada PC con su color, y un **historial de impresión** que demuestra el orden FIFO.

## Problemas

| Problema | Explicación |
|----------|-------------|
| `pop(0)` es O(n) | Al quitar el primer elemento de una lista, Python recorre todos los demás un lugar a la izquierda |
| Se pierden trabajos con la cola llena | Si llega un trabajo cuando ya hay 6, simplemente no se agrega |
| La capacidad se muestra con la constante | `mostrar_cola()` imprime `CAPACIDAD_MAXIMA` en vez de `cola.capacidad`; si se creara una cola de otro tamaño, el mensaje estaría mal |

## Solución

| Problema | Solución |
|----------|----------|
| `pop(0)` | Usar `collections.deque`, cuyo `popleft()` es O(1). Con capacidad 6 la diferencia no se nota, pero con miles de trabajos sí |
| Cola llena | El programa avisa "LLENA" para que el usuario imprima antes de mandar más, igual que una impresora real que rechaza trabajos cuando su memoria está llena |
| Capacidad | La ventana muestra el dibujo usando `cola.capacidad` |

## Forecast

- **Optimista:** se imprime al mismo ritmo en que llegan los trabajos; la cola nunca se llena y nadie espera mucho.
- **Probable:** en horas pico llegan más trabajos de los que se imprimen y la cola se llena por momentos, pero se vacía al imprimir.
- **Pesimista:** llegan trabajos más rápido de lo que se imprimen, la cola pasa casi siempre llena y muchos trabajos se rechazan.

## Conclusión

La cola es la estructura correcta para cualquier cosa que se deba atender **por turnos y de forma justa**, porque el primero que llega es el primero que sale. A diferencia de la pila del proyecto 1, donde sale el último que entró, aquí sale el primero. La capacidad limitada hace que el proyecto se parezca más a una impresora real, que tiene memoria finita.

## Fuentes

- Python Software Foundation. *Using Lists as Queues*. https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
- Python Software Foundation. *collections.deque*. https://docs.python.org/3/library/collections.html#collections.deque
- Erlang, A. K. (1909). The theory of probabilities and telephone conversations. *Nyt Tidsskrift for Matematik B, 20*, 33–39.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. (2022). *Introduction to Algorithms* (4.ª ed.), cap. 10 "Elementary Data Structures". MIT Press.
