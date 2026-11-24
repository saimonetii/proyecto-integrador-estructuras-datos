# Proyecto 1: Navegador web con Pilas

[← Volver al README](../README.md) · Código: [`proyectos/p1_navegador_web.py`](../proyectos/p1_navegador_web.py) · Ventana: [`interfaz/ventana_navegador.py`](../interfaz/ventana_navegador.py)

## Introducción

Hablaremos del primer proyecto: un navegador web que simula los botones **Back** (regresar) y **Forward** (avanzar). Todos usamos estos botones a diario, pero detrás hay una estructura de datos muy sencilla: la **pila**. Con dos pilas y una variable para la página actual se puede guardar todo el historial y moverse hacia atrás y hacia adelante.

## Origen

La pila es una de las estructuras más antiguas de la computación. Alan Turing ya usaba en 1946 los términos *bury* y *unbury* para entrar y regresar de subrutinas, y en 1955 Klaus Samelson y Friedrich L. Bauer propusieron formalmente la idea de la pila (la llamaron *Operationskeller*, "sótano de operaciones") y la patentaron en 1957. Hoy la pila está en todos lados: en el botón deshacer (Ctrl+Z), en las llamadas a funciones de cualquier lenguaje y, claro, en el historial del navegador.

## Funcionamiento

Una pila funciona como una pila de platos: el **último en entrar es el primero en salir** (LIFO, *Last In, First Out*). Solo se puede poner o quitar el elemento de arriba, que se llama **tope**.

### Clase `Pila`

La pila usa una lista de Python, y el **final de la lista es el tope**.

| Método | Qué hace | Cómo lo hace | Complejidad |
|--------|----------|--------------|-------------|
| `apilar(e)` | Pone un elemento en el tope | `self.elementos.append(e)` | O(1) |
| `desapilar()` | Quita y regresa el tope | `self.elementos.pop()` | O(1) |
| `ver_tope()` | Regresa el tope sin quitarlo | `self.elementos[-1]` | O(1) |
| `esta_vacia()` | Dice si no hay elementos | `len(self.elementos) == 0` | O(1) |
| `vaciar()` | Borra todo | `self.elementos = []` | O(1) |

### Clase `NavegadorWeb`

| Atributo | Para qué sirve |
|----------|----------------|
| `pila_atras` | Páginas visitadas **antes** de la actual |
| `pila_adelante` | Páginas de las que se regresó con Back, para poder hacer Forward |
| `pagina_actual` | La página que se está viendo |

| Acción | Qué pasa |
|--------|----------|
| Visitar `url` | La página actual se apila en **atrás**, la pila **adelante** se vacía y `url` pasa a ser la actual |
| Back | La actual se apila en **adelante** y la nueva actual es la que se desapila de **atrás** |
| Forward | La actual se apila en **atrás** y la nueva actual es la que se desapila de **adelante** |

### Ejemplo

| Paso | Página actual | Pila atrás (tope a la derecha) | Pila adelante |
|------|---------------|-------------------------------|---------------|
| Visitar google.com | google.com | [ ] | [ ] |
| Visitar github.com | github.com | [google.com] | [ ] |
| Visitar youtube.com | youtube.com | [google.com, github.com] | [ ] |
| Back | github.com | [google.com] | [youtube.com] |
| Back | google.com | [ ] | [youtube.com, github.com] |
| Forward | github.com | [google.com] | [youtube.com] |
| Visitar anahuac.mx | anahuac.mx | [google.com, github.com] | [ ] ← se vacía |

### En la interfaz

La ventana tiene los botones **◀ Back** y **Forward ▶**, un cuadro para escribir la URL y el botón **Visitar** (también funciona con Enter). Abajo se dibujan las dos pilas como cajas apiladas y el tope se marca en amarillo con la etiqueta **← TOPE**. Los botones Back y Forward se desactivan cuando su pila está vacía.

## Problemas

| Problema | Explicación |
|----------|-------------|
| `desapilar()` y `ver_tope()` truenan con la pila vacía | La clase `Pila` no revisa si está vacía antes de hacer `pop()` o `[-1]`, así que lanzaría un `IndexError` |
| El historial no tiene límite | Si se visitan miles de páginas, la pila `atrás` crece sin parar y ocupa cada vez más memoria |
| Mensajes con `print()` | Los métodos imprimen en la consola, lo cual no sirve dentro de una ventana |

## Solución

| Problema | Solución |
|----------|----------|
| Pila vacía | `NavegadorWeb` siempre revisa `esta_vacia()` antes de desapilar, y la ventana además desactiva los botones, así que nunca se llega al error |
| Historial sin límite | Para este proyecto no es necesario, pero se podría limitar a cierto número de páginas como hacen los navegadores reales |
| `print()` | La ventana muestra sus propios mensajes en la barra de estado y dibuja las pilas leyendo `pila_atras.elementos` y `pila_adelante.elementos` |

## Forecast

- **Optimista:** todas las operaciones (visitar, Back y Forward) son O(1), así que el navegador responde igual de rápido con 3 páginas que con 3,000.
- **Probable:** el usuario visita algunas decenas de páginas y se mueve con Back y Forward; Python agranda la lista de vez en cuando, pero el costo promedio sigue siendo O(1).
- **Pesimista:** con un historial enorme el problema no es la velocidad sino la memoria, porque la pila crece sin límite.

## Conclusión

La pila es una estructura muy simple, pero resuelve el historial del navegador de forma elegante: con dos pilas se puede ir y regresar sin perder ninguna página, y todas las operaciones son O(1). Algo importante del proyecto es la regla de **vaciar la pila adelante al visitar una página nueva**, porque al abrir una página nueva el historial toma otro camino y las páginas "siguientes" ya no tienen sentido.

## Fuentes

- Python Software Foundation. *Using Lists as Stacks*. https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
- Samelson, K. y Bauer, F. L. (1960). Sequential formula translation. *Communications of the ACM, 3*(2), 76–83.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. (2022). *Introduction to Algorithms* (4.ª ed.), cap. 10 "Elementary Data Structures". MIT Press.
