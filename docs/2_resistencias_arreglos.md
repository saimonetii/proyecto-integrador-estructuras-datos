# Proyecto 2: Resistencias eléctricas con Arreglos y Listas

[← Volver al README](../README.md) · Código: [`proyectos/p2_resistencias.py`](../proyectos/p2_resistencias.py)

## Introducción

Hablaremos del segundo proyecto, que une la programación con la electrónica. Las resistencias tienen bandas de colores que indican su valor en ohmios, y este programa hace dos cosas: a partir de un valor muestra sus **tres bandas de color**, y genera **n resistencias aleatorias** para calcular su resistencia equivalente **en serie** y **en paralelo**. La estructura principal son los **arreglos** (listas de Python) y las **tuplas**. Este proyecto ya tenía interfaz gráfica con Tkinter desde su entrega.

## Origen

Las resistencias son tan pequeñas que no se les puede imprimir el número, por eso se usa un código de colores, estandarizado hoy en la norma internacional **IEC 60062**. Cada color representa un dígito del 0 al 9. Como los colores van en orden y cada uno corresponde a un número, la forma natural de guardarlos en un programa es un **arreglo**, donde el índice es el dígito.

## Funcionamiento

### Arreglos paralelos

La clase `Resistencia` tiene dos arreglos del mismo tamaño. Se llaman **paralelos** porque la misma posición habla del mismo color:

| Índice (dígito) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-----------------|---|---|---|---|---|---|---|---|---|---|
| `colores` | Negro | Marrón | Rojo | Naranja | Amarillo | Verde | Azul | Violeta | Gris | Blanco |
| `codigos_hex` | #000000 | #8B4513 | #FF0000 | #FFA500 | #FFFF00 | #008000 | #0000FF | #EE82EE | #808080 | #FFFFFF |

Acceder a un arreglo por su índice es **O(1)**: no hay que buscar nada, se va directo a la posición.

### Métodos

| Método | Qué hace | Complejidad |
|--------|----------|-------------|
| `obtener_colores(valor)` | Regresa dos tuplas: los nombres de las 3 bandas y sus colores hexadecimales | O(d), d = número de dígitos |
| `generar_resistencias_aleatorias(n)` | Crea una lista de `n` valores aleatorios entre 10 y 1,000,000,000 Ω | O(n) |
| `sumar_serie(lista)` | Rt = R1 + R2 + … + Rn | O(n) |
| `sumar_paralelo(lista)` | 1/Rt = 1/R1 + 1/R2 + … + 1/Rn | O(n) |

### Cómo se obtienen las bandas

| Banda | Significado | Ejemplo con 4700 Ω |
|-------|-------------|--------------------|
| 1.ª | Primer dígito | 4 → **Amarillo** |
| 2.ª | Segundo dígito | 7 → **Violeta** |
| 3.ª (multiplicador) | Cuántos ceros siguen (`len(valor) - 2`) | 2 ceros → **Rojo** |

```python
valor_str = str(valor)                  # "4700"
digito1 = int(valor_str[0])             # 4
digito2 = int(valor_str[1])             # 7
multiplicador = len(valor_str) - 2      # 2
```

### Serie y paralelo

| Conexión | Fórmula | Resultado |
|----------|---------|-----------|
| Serie | Rt = R1 + R2 + … + Rn | Siempre es **mayor** que la resistencia más grande |
| Paralelo | Rt = 1 / (1/R1 + 1/R2 + … + 1/Rn) | Siempre es **menor** que la resistencia más chica |

### En la interfaz

Se escriben el valor y la cantidad `n` y se presiona **Calcular**. Las tres etiquetas se pintan con el color de cada banda (el texto va en blanco cuando el fondo es negro) y abajo aparecen la lista de resistencias y las dos sumas.

## Problemas

| Problema | Explicación |
|----------|-------------|
| Valores menores a 100 no se aceptan | Con 3 bandas el multiplicador mínimo es 1 (un cero), así que 47 Ω o 10 Ω marcan error aunque existen en la vida real |
| Solo se usan 2 cifras | 4750 Ω se muestra igual que 4700 Ω, porque las bandas guardan solo los dos primeros dígitos |
| Máximo 11 dígitos | Si el multiplicador es mayor que 9 ya no hay color para él |
| No se podía importar en el integrador | El archivo crea su ventana `tk.Tk()` desde el inicio, así que al importarlo se abría solo |

## Solución

| Problema | Solución |
|----------|----------|
| Valores menores a 100 | En las resistencias reales se usa una banda **dorada** (×0.1) o **plateada** (×0.01) como multiplicador; se podría agregar a los arreglos |
| Solo 2 cifras | Existe el código de **4 bandas** (3 cifras + multiplicador) para mayor precisión |
| Máximo 11 dígitos | Se valida y se muestra un mensaje de error |
| Importar en el integrador | `Main1.py` ejecuta el archivo original en su propio proceso con `subprocess`, sin modificarlo |

## Forecast

- **Optimista:** el valor tiene exactamente dos cifras significativas (por ejemplo 4700 o 220,000) y las bandas lo representan exacto.
- **Probable:** el valor tiene más cifras (por ejemplo 4750) y las bandas lo redondean hacia abajo a 2 cifras; las sumas en serie y paralelo salen bien porque recorren la lista una sola vez, O(n).
- **Pesimista:** el valor tiene menos de 3 dígitos o más de 11 y no se puede representar con 3 bandas.

## Conclusión

Este proyecto demuestra que un **arreglo** es la estructura ideal cuando los datos tienen una posición fija: el dígito es directamente el índice, así que obtener el color es inmediato. Las **tuplas** sirven para regresar resultados que no deben cambiar y las **listas** para guardar un número variable de resistencias y sumarlas.

## Fuentes

- International Electrotechnical Commission. *IEC 60062: Marking codes for resistors and capacitors*.
- Python Software Foundation. *Data Structures: Lists and Tuples*. https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Python Software Foundation. *random — Generate pseudo-random numbers*. https://docs.python.org/3/library/random.html
