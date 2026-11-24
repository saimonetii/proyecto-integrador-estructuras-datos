# Proyecto 5: Directorio de alumnos con Árbol Binario de Búsqueda

[← Volver al README](../README.md) · Código: [`proyectos/p5_arbol_alumnos.py`](../proyectos/p5_arbol_alumnos.py) · Ventana: [`interfaz/ventana_arbol.py`](../interfaz/ventana_arbol.py)

## Introducción

Hablaremos del quinto proyecto: un directorio de alumnos que guarda la **matrícula** y el **nombre** de cada uno en un **árbol binario de búsqueda** (ABB). A diferencia de las estructuras anteriores, que eran lineales, el árbol es una estructura **jerárquica**: permite buscar mucho más rápido que una lista y además mantiene los datos ordenados. El programa permite insertar, buscar, eliminar, ver los tres recorridos y algunas estadísticas.

## Origen

El árbol binario de búsqueda apareció en **1960**, cuando Conway Berners-Lee y David Wheeler lo usaron para guardar datos etiquetados en cintas magnéticas. Al mismo tiempo, P. F. Windley, Andrew Donald Booth, Andrew Colin y Thomas N. Hibbard lo descubrieron por su cuenta. La idea es la misma que la de la búsqueda binaria: en cada paso se descarta la mitad de los datos. Hoy se usa en bases de datos, sistemas de archivos y en los diccionarios ordenados de muchos lenguajes.

## Funcionamiento

### Conceptos

| Concepto | Significado |
|----------|-------------|
| Nodo | Cada alumno guardado (matrícula, nombre, hijo izquierdo y derecho) |
| Raíz | El primer nodo, el de hasta arriba |
| Hoja | Un nodo sin hijos |
| Altura | Número de niveles del árbol |
| Regla del ABB | Todo lo del lado **izquierdo** es **menor** y todo lo del lado **derecho** es **mayor** |

### Árbol de ejemplo

El programa empieza con 7 alumnos para que el árbol no esté vacío:

```
              50 Ana
            /        \
       30 Luis      70 Sofia
       /    \        /     \
  20 Carlos 40 Maria 60 Jorge 80 Valeria
```

### Clases y métodos

| Método | Qué hace | Complejidad (balanceado / peor caso) |
|--------|----------|--------------------------------------|
| `insertar(matricula, nombre)` | Baja desde la raíz (menor → izquierda, mayor → derecha) hasta un hueco; regresa `False` si la matrícula ya existe | O(log n) / O(n) |
| `buscar(matricula)` | Baja igual que insertar y regresa el nodo y el **camino recorrido** | O(log n) / O(n) |
| `eliminar(matricula)` | Quita el nodo según los 3 casos | O(log n) / O(n) |
| `inorden()`, `preorden()`, `postorden()` | Recorridos recursivos | O(n) |
| `altura()` | `1 + max(altura izquierda, altura derecha)` | O(n) |
| `minimo()` / `maximo()` | Bajar siempre a la izquierda / derecha | O(log n) / O(n) |

### Los 3 casos de eliminar

| Caso | Qué se hace | Ejemplo |
|------|-------------|---------|
| 1. El nodo es hoja | Se quita y ya | Eliminar 20 |
| 2. Tiene un hijo | El hijo toma su lugar | Eliminar 30 después de quitar el 20 → el 40 sube |
| 3. Tiene dos hijos | Se reemplaza por su **sucesor** (el menor del subárbol derecho) y luego se elimina el sucesor | Eliminar 50 → el 60 pasa a ser la raíz |

### Recorridos

| Recorrido | Orden | Resultado con el árbol de ejemplo | Para qué sirve |
|-----------|-------|-----------------------------------|----------------|
| Inorden | Izquierdo → Raíz → Derecho | 20, 30, 40, 50, 60, 70, 80 | Sale **ordenado** |
| Preorden | Raíz → Izquierdo → Derecho | 50, 30, 20, 40, 70, 60, 80 | Copiar el árbol con la misma forma |
| Postorden | Izquierdo → Derecho → Raíz | 20, 40, 30, 60, 80, 70, 50 | Borrar el árbol (primero los hijos) |

### En la interfaz

A la izquierda están los campos de matrícula y nombre con los botones Insertar, Buscar y Eliminar, los tres recorridos y las estadísticas. A la derecha se dibuja el árbol: cada nodo se coloca en **x** según su posición en inorden (así nunca se enciman) y en **y** según su nivel. Buscar pinta el camino en azul y el nodo encontrado en amarillo, y los recorridos se animan nodo por nodo con su número de visita.

## Problemas

| Problema | Explicación |
|----------|-------------|
| El árbol se puede desbalancear | Si las matrículas se insertan ya ordenadas (10, 20, 30, 40…), cada nodo queda a la derecha del anterior y el árbol se vuelve una "lista", con búsquedas O(n) |
| Límite de recursión | Los recorridos y `eliminar` son recursivos; Python permite cerca de 1,000 llamadas anidadas, así que un árbol muy desbalanceado con más de 1,000 niveles daría `RecursionError` |
| No acepta matrículas repetidas | Si se intenta insertar una matrícula que ya existe, se rechaza |

## Solución

| Problema | Solución |
|----------|----------|
| Desbalance | Usar árboles que se balancean solos, como los **AVL** o los **rojo-negro**, que garantizan O(log n) |
| Recursión | Con árboles balanceados la altura es pequeña (un árbol de un millón de nodos tiene unos 20 niveles); también se pueden escribir los recorridos con una pila en lugar de recursión |
| Repetidas | Es lo correcto: la matrícula identifica a un solo alumno, por eso `insertar` regresa `False` y el programa avisa |

## Forecast

- **Optimista:** el árbol está balanceado y cada búsqueda descarta la mitad de los alumnos: con 1,000 alumnos se encuentra cualquiera en unas 10 comparaciones, O(log n).
- **Probable:** las matrículas llegan en orden aleatorio y el árbol queda casi balanceado, con un costo muy cercano a O(log n).
- **Pesimista:** las matrículas llegan ordenadas y el árbol se vuelve una línea: con 1,000 alumnos una búsqueda puede tomar 1,000 comparaciones, O(n).

## Conclusión

El árbol binario de búsqueda combina dos ventajas: busca rápido, como un arreglo ordenado, y permite insertar y eliminar sin mover todos los datos, como una lista. Con una sola regla (menores a la izquierda y mayores a la derecha) se obtienen búsquedas en O(log n) y datos siempre ordenados con el recorrido inorden. Su debilidad es el desbalance, y por eso existen versiones mejoradas como los árboles AVL.

## Fuentes

- Hibbard, T. N. (1962). Some combinatorial properties of certain trees with applications to searching and sorting. *Journal of the ACM, 9*(1), 13–28.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. (2022). *Introduction to Algorithms* (4.ª ed.), cap. 12 "Binary Search Trees". MIT Press.
- Knuth, D. E. (1998). *The Art of Computer Programming, Vol. 3: Sorting and Searching* (2.ª ed.), sección 6.2.2 "Binary Tree Searching". Addison-Wesley.
- Python Software Foundation. *sys.getrecursionlimit*. https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
