# Directorio de alumnos con árbol binario de búsqueda

## Introducción

En este proyecto hicimos un directorio de alumnos que guarda la matrícula y el nombre de cada uno en un árbol binario de búsqueda. A diferencia de las estructuras de los proyectos anteriores, que eran lineales, el árbol es una estructura jerárquica que permite buscar mucho más rápido que una lista y además mantiene los datos ordenados. El programa permite insertar, buscar y eliminar alumnos, ver los tres recorridos del árbol y algunas estadísticas.

## El árbol binario de búsqueda

Un árbol binario está formado por nodos, y cada nodo puede tener como máximo dos hijos, uno a la izquierda y otro a la derecha. El nodo de hasta arriba se llama raíz y los nodos que no tienen hijos se llaman hojas. Es de búsqueda porque cumple una regla en todos sus nodos: todo lo que está del lado izquierdo es menor y todo lo que está del lado derecho es mayor.

Gracias a esa regla no hay que revisar todos los datos para encontrar uno, porque en cada nodo se decide si ir a la izquierda o a la derecha y se descarta la otra mitad. El árbol binario de búsqueda apareció en 1960 y lo descubrieron varias personas al mismo tiempo, entre ellas Thomas N. Hibbard, que publicó un estudio sobre él en 1962. Hoy se usa en bases de datos, sistemas de archivos y en los diccionarios ordenados de muchos lenguajes.

El programa empieza con siete alumnos de ejemplo para que el árbol no esté vacío:

```
              50 Ana
            /        \
       30 Luis      70 Sofia
       /    \        /     \
  20 Carlos 40 Maria 60 Jorge 80 Valeria
```

## Cómo funciona el código

La clase `Nodo` guarda la matrícula, el nombre y las referencias a sus dos hijos. La clase `ArbolBinarioBusqueda` guarda la raíz y la cantidad de alumnos.

| Método | Qué hace | Si está balanceado | En el peor caso |
|--------|----------|--------------------|-----------------|
| `insertar` | Baja desde la raíz, a la izquierda si es menor y a la derecha si es mayor, hasta encontrar un lugar vacío. Si la matrícula ya existe no la agrega | O(log n) | O(n) |
| `buscar` | Baja igual que insertar y regresa el alumno y el camino que recorrió | O(log n) | O(n) |
| `eliminar` | Quita al alumno según el caso en el que esté | O(log n) | O(n) |
| `inorden`, `preorden`, `postorden` | Recorren todo el árbol | O(n) | O(n) |
| `altura` | Cuenta los niveles del árbol | O(n) | O(n) |
| `minimo` y `maximo` | Bajan siempre a la izquierda o siempre a la derecha | O(log n) | O(n) |

Para eliminar hay tres casos:

| Caso | Qué se hace | Ejemplo |
|------|-------------|---------|
| El nodo no tiene hijos | Se quita y ya | Eliminar el 20 |
| El nodo tiene un hijo | El hijo toma su lugar | Eliminar el 30 después de quitar el 20, y el 40 sube |
| El nodo tiene dos hijos | Se reemplaza por su sucesor, que es el menor del lado derecho, y después se elimina el sucesor | Eliminar el 50, y el 60 se vuelve la raíz |

Los recorridos visitan todos los nodos en distinto orden:

| Recorrido | Orden de visita | Resultado con el árbol de ejemplo | Para qué sirve |
|-----------|-----------------|-----------------------------------|----------------|
| Inorden | Izquierda, raíz, derecha | 20, 30, 40, 50, 60, 70, 80 | Saca los datos ordenados |
| Preorden | Raíz, izquierda, derecha | 50, 30, 20, 40, 70, 60, 80 | Copiar el árbol con la misma forma |
| Postorden | Izquierda, derecha, raíz | 20, 40, 30, 60, 80, 70, 50 | Borrar el árbol empezando por los hijos |

## Ejemplo paso a paso

Si se inserta la matrícula 65, el programa la compara con la raíz: 65 es mayor que 50, así que va a la derecha. Luego 65 es menor que 70, así que va a la izquierda. Después 65 es mayor que 60, y como el lado derecho del 60 está vacío, ahí se queda. Si después se busca el 65, el camino recorrido es 50, 70, 60, 65, y se encuentra en cuatro comparaciones.

## La ventana del proyecto

A la izquierda están los cuadros para escribir la matrícula y el nombre, los botones Insertar, Buscar y Eliminar, los botones de los tres recorridos y las estadísticas. A la derecha se dibuja el árbol. Cada nodo se acomoda de izquierda a derecha según su lugar en el recorrido inorden, así nunca se enciman, y de arriba hacia abajo según su nivel. Al buscar se pinta de azul el camino y de amarillo el alumno encontrado, y los recorridos se animan nodo por nodo mostrando el número de visita.

## Detalles a tener en cuenta

- Si las matrículas se insertan ya ordenadas, como 10, 20, 30 y 40, cada nodo queda a la derecha del anterior y el árbol se vuelve una línea. En ese caso buscar ya no es rápido. Para evitarlo existen árboles que se balancean solos, como los AVL.
- Los recorridos son recursivos, es decir, el método se llama a sí mismo. Python permite alrededor de mil llamadas anidadas, así que solo sería un problema con un árbol muy desbalanceado.
- No se permiten matrículas repetidas, porque cada matrícula identifica a un solo alumno.

## Preguntas que nos pueden hacer en la exposición

- **¿Por qué el recorrido inorden sale ordenado?** Porque primero visita todo lo menor, luego el nodo y al final todo lo mayor.
- **¿Por qué en el caso de dos hijos se usa el sucesor?** Porque es el valor más pequeño que es mayor que el nodo, así que al ponerlo en su lugar se sigue cumpliendo la regla del árbol.
- **¿Qué ventaja tiene sobre una lista?** En una lista buscar es O(n) y en un árbol balanceado es O(log n). Con mil alumnos, la lista puede tardar mil comparaciones y el árbol unas diez.

## Conclusión

El árbol binario de búsqueda combina lo mejor de dos estructuras: busca rápido como un arreglo ordenado y permite insertar y eliminar sin mover todos los datos como una lista. Con una sola regla, menores a la izquierda y mayores a la derecha, se consiguen búsquedas muy rápidas y datos siempre ordenados. Su punto débil es que se puede desbalancear, y por eso existen versiones mejoradas como los árboles AVL.

## Fuentes

- Hibbard, T. N. Some combinatorial properties of certain trees with applications to searching and sorting. *Journal of the ACM*, vol. 9, núm. 1, pp. 13–28, 1962.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*, 4.ª edición, capítulo 12. MIT Press, 2022.
- Knuth, D. E. *The Art of Computer Programming, Vol. 3: Sorting and Searching*, 2.ª edición, sección 6.2.2. Addison-Wesley, 1998.
