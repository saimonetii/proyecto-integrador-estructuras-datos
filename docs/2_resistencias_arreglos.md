# Resistencias eléctricas con arreglos y listas

## Introducción

En este proyecto unimos la programación con la electrónica. Las resistencias tienen bandas de colores que indican su valor en ohmios, y el programa hace dos cosas: a partir de un valor muestra sus tres bandas de color, y genera una cantidad de resistencias aleatorias para calcular su resistencia equivalente en serie y en paralelo. Las estructuras que se usan son los arreglos, las tuplas y las listas. Este proyecto ya tenía interfaz gráfica con Tkinter desde que se entregó, así que el menú principal lo abre tal cual.

## El código de colores y los arreglos

Las resistencias son tan pequeñas que no se les puede imprimir el número, por eso se usa un código de colores que hoy está definido en la norma internacional IEC 60062. Cada color representa un dígito del 0 al 9 y siempre van en el mismo orden. Por eso la forma más natural de guardarlos en un programa es un arreglo, donde la posición de cada color es su dígito.

La clase `Resistencia` tiene dos arreglos del mismo tamaño. Se les llama arreglos paralelos porque la misma posición habla del mismo color: uno guarda el nombre y el otro el código hexadecimal que se usa para pintarlo en la ventana.

| Dígito | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|--------|---|---|---|---|---|---|---|---|---|---|
| `colores` | Negro | Marrón | Rojo | Naranja | Amarillo | Verde | Azul | Violeta | Gris | Blanco |
| `codigos_hex` | #000000 | #8B4513 | #FF0000 | #FFA500 | #FFFF00 | #008000 | #0000FF | #EE82EE | #808080 | #FFFFFF |

La ventaja de un arreglo es que llegar a una posición es inmediato. No hay que buscar el color, se va directo al índice.

## Cómo funciona el código

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `obtener_colores(valor)` | Regresa dos tuplas, una con los nombres de las tres bandas y otra con sus colores | O(d), donde d es el número de dígitos |
| `generar_resistencias_aleatorias(n)` | Crea una lista con n valores aleatorios entre 10 y 1,000,000,000 ohmios | O(n) |
| `sumar_serie(lista)` | Suma todas las resistencias | O(n) |
| `sumar_paralelo(lista)` | Suma los inversos y saca el inverso del resultado | O(n) |

Para obtener las bandas, el valor se convierte en texto. La primera banda es el primer dígito, la segunda banda es el segundo dígito y la tercera banda es el multiplicador, que es la cantidad de ceros que siguen.

| Banda | Qué representa | Ejemplo con 4700 ohmios |
|-------|----------------|-------------------------|
| Primera | Primer dígito | 4, Amarillo |
| Segunda | Segundo dígito | 7, Violeta |
| Tercera | Número de ceros | 2 ceros, Rojo |

```python
valor_str = str(valor)                  # "4700"
digito1 = int(valor_str[0])             # 4
digito2 = int(valor_str[1])             # 7
multiplicador = len(valor_str) - 2      # 2
```

Para las sumas se usan las fórmulas de la clase de circuitos:

| Conexión | Fórmula | Qué se observa |
|----------|---------|----------------|
| Serie | Rt = R1 + R2 + … + Rn | El resultado siempre es mayor que la resistencia más grande |
| Paralelo | 1/Rt = 1/R1 + 1/R2 + … + 1/Rn | El resultado siempre es menor que la resistencia más chica |

## La ventana del proyecto

Se escribe el valor de la resistencia y la cantidad de resistencias que se quieren generar, y se presiona Calcular. Las tres etiquetas se pintan con el color de cada banda y el texto se pone en blanco cuando el fondo es negro para que se pueda leer. Abajo aparecen la lista de resistencias generadas y las dos sumas.

## Detalles a tener en cuenta

- Los valores menores a 100 no se aceptan, porque con tres bandas el multiplicador mínimo es un cero. En las resistencias reales se usan bandas doradas o plateadas para los valores pequeños.
- Solo se usan los dos primeros dígitos, así que 4750 se muestra igual que 4700. Así funciona el código de tres bandas; para más precisión existe el de cuatro bandas.
- Si el valor tiene más de 11 dígitos ya no hay color para el multiplicador y el programa muestra un mensaje de error.
- Cuando se escribe algo que no es número, el programa lo detecta y pide números válidos.

## Preguntas que nos pueden hacer en la exposición

- **¿Dónde están los arreglos?** En `colores` y `codigos_hex`, que son arreglos paralelos. Las bandas se regresan como tuplas y las resistencias aleatorias se guardan en una lista.
- **¿Por qué 4700 da Amarillo, Violeta y Rojo?** Porque el 4 es amarillo, el 7 es violeta y después vienen dos ceros, y el 2 es rojo.
- **¿Por qué en paralelo el resultado es tan pequeño?** Porque al conectar resistencias en paralelo la corriente tiene más caminos para pasar, y eso siempre da una resistencia menor que la más chica.

## Conclusión

Este proyecto demuestra que el arreglo es la estructura ideal cuando los datos tienen una posición fija, porque el dígito es directamente el índice y obtener el color es inmediato. Las tuplas sirven para regresar resultados que no deben cambiar y las listas para guardar una cantidad variable de resistencias y recorrerlas para sumarlas.

## Fuentes

- International Electrotechnical Commission. *IEC 60062: Marking codes for resistors and capacitors*.
- Python Software Foundation. *Data Structures: Lists and Tuples*. https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Python Software Foundation. *random — Generate pseudo-random numbers*. https://docs.python.org/3/library/random.html
