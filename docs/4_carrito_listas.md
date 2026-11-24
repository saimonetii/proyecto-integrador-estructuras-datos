# Carrito de compras con listas de objetos

## Introducción

En este proyecto hicimos un sistema de carrito de compras como el de cualquier tienda en línea. Hay un catálogo de productos y un carrito donde se agrega lo que se quiere comprar. Se puede buscar un producto por su ID o por su nombre, cambiar cantidades, eliminar productos, vaciar el carrito y finalizar la compra con el total a pagar. Las estructuras que se usan son las listas de objetos y la búsqueda lineal.

## Las listas de objetos

En un carrito cada línea no es un solo dato, sino un producto con su cantidad y su subtotal. Por eso no basta con una lista de números y se necesita una lista de objetos, donde cada objeto agrupa sus datos y también sus propios métodos. En Python las listas pueden crecer todo lo que se necesite y guardar cualquier tipo de objeto, así que son perfectas para este problema.

## Cómo funciona el código

El programa tiene cuatro clases:

| Clase | Qué guarda | Qué representa |
|-------|------------|----------------|
| `Producto` | ID, nombre y precio | Un producto del catálogo |
| `ElementoCarrito` | Un producto y su cantidad, y calcula su subtotal | Una línea del carrito |
| `Carrito` | Una lista de `ElementoCarrito` | El carrito completo |
| `SistemaCarrito` | El catálogo, que es una lista de `Producto`, y el carrito | El programa con su menú |

`Producto` y `ElementoCarrito` usan `@dataclass`, que hace que Python genere automáticamente el constructor con los atributos que se declaran.

El catálogo tiene cinco productos:

| ID | Producto | Precio |
|----|----------|--------|
| 101 | Leche | $28.50 |
| 102 | Pan integral | $42.00 |
| 103 | Huevos | $58.00 |
| 104 | Arroz | $31.50 |
| 105 | Manzanas | $49.90 |

Todas las búsquedas son lineales, es decir, revisan los elementos uno por uno hasta encontrar el que buscan:

| Método | Dónde busca | Cómo compara |
|--------|-------------|--------------|
| `buscar_producto_por_id` | Catálogo | El ID tiene que ser igual |
| `buscar_productos_por_nombre` | Catálogo | El texto tiene que estar dentro del nombre, sin importar mayúsculas |
| `Carrito.buscar_por_id` | Carrito | El ID tiene que ser igual |
| `Carrito.buscar_por_nombre` | Carrito | El nombre tiene que ser exacto, sin importar mayúsculas |

Y estas son las operaciones del carrito:

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `agregar_producto` | Si el producto ya está en el carrito suma la cantidad, si no agrega una línea nueva | O(n) |
| `modificar_cantidad` | Cambia la cantidad de una línea | O(1) |
| `eliminar_producto` | Quita una línea del carrito | O(n) |
| `vaciar` | Borra todo el carrito | O(n) |
| `calcular_total` | Suma el subtotal de cada línea, que es precio por cantidad | O(n) |

## Ejemplo paso a paso

| Acción | Carrito | Total |
|--------|---------|-------|
| Agregar 2 Leche | Leche por 2 = $57.00 | $57.00 |
| Agregar 1 Huevos | Leche por 2, Huevos por 1 | $115.00 |
| Agregar 1 Leche otra vez | Leche por 3 = $85.50, Huevos por 1 | $143.50 |

Cuando se agrega un producto que ya estaba no se crea otra línea, solo aumenta la cantidad.

## La ventana del proyecto

A la izquierda está el catálogo en una tabla con un cuadro de búsqueda que filtra mientras se escribe. Si se escribe un número busca por ID y si se escribe texto busca por nombre. A la derecha está el carrito con la cantidad, el precio unitario y el subtotal de cada producto, y los botones Modificar, Eliminar, Vaciar carrito y Finalizar compra, que muestra el resumen con el total a pagar.

## Detalles a tener en cuenta

- La búsqueda lineal es fácil de programar y con cinco productos es instantánea, pero con miles de productos sería lenta. En ese caso convendría usar un diccionario con el ID como llave.
- Los precios se guardan como números decimales de tipo `float`, que pueden tener pequeños errores de redondeo. Como los totales se muestran con dos decimales, el error no se ve.
- En el catálogo se puede buscar con una parte del nombre, pero en el carrito se necesita el nombre exacto. En la ventana esto no importa porque el producto se elige con un clic.


## Conclusión

Las listas de objetos permiten representar cosas reales que tienen varios datos juntos, como un producto con su precio o una línea del carrito con su cantidad, y cada objeto puede tener su propio comportamiento. La búsqueda lineal es sencilla y suficiente para un catálogo pequeño, y es importante saber que su costo crece conforme crece el número de productos.

## Fuentes

- Python Software Foundation. *dataclasses — Data Classes*. https://docs.python.org/3/library/dataclasses.html
- Python Software Foundation. *Data Structures: More on Lists*. https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *Floating-Point Arithmetic: Issues and Limitations*. https://docs.python.org/3/tutorial/floatingpoint.html
- Knuth, D. E. *The Art of Computer Programming, Vol. 3: Sorting and Searching*, 2.ª edición, sección 6.1. Addison-Wesley, 1998.
