# Proyecto 4: Carrito de compras con Listas de objetos

[← Volver al README](../README.md) · Código: [`proyectos/p4_carrito_compras.py`](../proyectos/p4_carrito_compras.py) · Ventana: [`interfaz/ventana_carrito.py`](../interfaz/ventana_carrito.py)

## Introducción

Hablaremos del cuarto proyecto: un sistema de carrito de compras como el de cualquier tienda en línea. Hay un **catálogo** de productos y un **carrito** donde el cliente agrega lo que quiere comprar; se puede buscar por ID o por nombre, cambiar cantidades, eliminar productos, vaciar el carrito y finalizar la compra con el total a pagar. La estructura principal son las **listas de objetos** y la **búsqueda lineal**.

## Origen

El carrito de compras es uno de los problemas más comunes en el comercio electrónico: cada línea del carrito no es un solo dato, sino un producto con su cantidad y su subtotal. Por eso no basta con una lista de números; se necesita una **lista de objetos**, donde cada objeto agrupa sus datos y sus propios métodos. En Python, las listas son arreglos dinámicos que pueden crecer y guardar cualquier tipo de objeto.

## Funcionamiento

### Clases

| Clase | Atributos | Métodos | Qué representa |
|-------|-----------|---------|----------------|
| `Producto` (`@dataclass`) | `id_producto`, `nombre`, `precio` | — | Un producto del catálogo |
| `ElementoCarrito` (`@dataclass`) | `producto`, `cantidad` | `calcular_subtotal()`, `actualizar_cantidad()` | Una línea del carrito |
| `Carrito` | `elementos` (lista de `ElementoCarrito`) | buscar, agregar, modificar, eliminar, vaciar, totales | El carrito completo |
| `SistemaCarrito` | `catalogo` (lista de `Producto`), `carrito` | menú, búsquedas en el catálogo | El programa |

`@dataclass` hace que Python genere automáticamente el `__init__` con los atributos declarados.

### Catálogo

| ID | Producto | Precio |
|----|----------|--------|
| 101 | Leche | $28.50 |
| 102 | Pan integral | $42.00 |
| 103 | Huevos | $58.00 |
| 104 | Arroz | $31.50 |
| 105 | Manzanas | $49.90 |

### Búsquedas (todas lineales)

| Método | Dónde busca | Criterio | Regresa |
|--------|-------------|----------|---------|
| `buscar_producto_por_id` | Catálogo | ID igual | Un producto o `None` |
| `buscar_productos_por_nombre` | Catálogo | El texto **está dentro** del nombre, sin importar mayúsculas (`casefold()`) | Lista de coincidencias |
| `Carrito.buscar_por_id` | Carrito | ID igual | Un elemento o `None` |
| `Carrito.buscar_por_nombre` | Carrito | Nombre **exacto**, sin importar mayúsculas | Un elemento o `None` |

### Operaciones del carrito

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `agregar_producto(p, cant)` | Si el producto ya está, suma la cantidad; si no, agrega una línea nueva | O(n) |
| `modificar_cantidad(el, cant)` | Cambia la cantidad de una línea | O(1) |
| `eliminar_producto(el)` | Quita la línea (`remove`) | O(n) |
| `vaciar()` | Borra todo (`clear`) | O(n) |
| `calcular_total()` | Suma de los subtotales (`precio × cantidad`) | O(n) |

### Ejemplo

| Acción | Carrito | Total |
|--------|---------|-------|
| Agregar 2 Leche | Leche ×2 = $57.00 | $57.00 |
| Agregar 1 Huevos | Leche ×2, Huevos ×1 | $115.00 |
| Agregar 1 Leche otra vez | Leche ×**3** = $85.50, Huevos ×1 | $143.50 |

### En la interfaz

A la izquierda está el catálogo en una tabla con un cuadro de búsqueda que filtra mientras se escribe (si se escribe un número busca por ID y si se escribe texto busca por nombre). A la derecha está el carrito con cantidad, precio unitario y subtotal, con los botones Modificar, Eliminar, Vaciar carrito y Finalizar compra.

## Problemas

| Problema | Explicación |
|----------|-------------|
| Búsqueda lineal | Para encontrar un producto se revisan uno por uno; con 5 productos no importa, pero con miles sería lento |
| Precios con `float` | Los decimales en `float` pueden tener pequeños errores de redondeo (por ejemplo 0.1 + 0.2 = 0.30000000000000004) |
| Búsquedas distintas | En el catálogo se busca por parte del nombre, pero en el carrito se necesita el nombre exacto |
| Finalizar no vacía el carrito | Después del resumen final, el carrito sigue con los mismos productos |

## Solución

| Problema | Solución |
|----------|----------|
| Búsqueda lineal | Usar un diccionario `{id: producto}`, donde buscar por ID es O(1) |
| Precios con `float` | Usar `decimal.Decimal` para dinero; en este proyecto los totales se muestran con 2 decimales (`:.2f`), así que el error no se ve |
| Búsquedas distintas | En la ventana el producto del carrito se elige con un clic en la tabla, así que no hay que escribir el nombre |
| Finalizar | La ventana muestra el resumen y deja que el usuario decida si vacía el carrito |

## Forecast

- **Optimista:** el producto buscado es el primero de la lista y se encuentra en 1 comparación, O(1).
- **Probable:** en promedio se revisa la mitad de la lista, n/2 comparaciones, que sigue siendo O(n).
- **Pesimista:** el producto es el último o no existe y se revisa toda la lista, O(n). Con un catálogo de miles de productos convendría cambiar a un diccionario.

## Conclusión

Las listas de objetos permiten modelar cosas reales que tienen varios datos juntos, como un producto con su precio o una línea del carrito con su cantidad. Además, cada objeto puede tener su propio comportamiento, como `calcular_subtotal()`. La búsqueda lineal es fácil de programar y suficiente para catálogos pequeños, pero hay que saber que su costo crece con el número de productos.

## Fuentes

- Python Software Foundation. *dataclasses — Data Classes*. https://docs.python.org/3/library/dataclasses.html
- Python Software Foundation. *Data Structures: More on Lists*. https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *Floating-Point Arithmetic: Issues and Limitations*. https://docs.python.org/3/tutorial/floatingpoint.html
- Knuth, D. E. (1998). *The Art of Computer Programming, Vol. 3: Sorting and Searching* (2.ª ed.), sección 6.1 "Sequential Searching". Addison-Wesley.
