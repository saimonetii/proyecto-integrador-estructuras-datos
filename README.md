# Proyecto Integrador de Estructuras de Datos

## Introducción

En este proyecto juntamos en un solo programa los seis proyectos que hicimos durante el semestre en la materia de Estructuras de Datos. Cada uno trabaja con una estructura distinta: pilas, arreglos, colas, listas, árboles y grafos. El programa está hecho en Python con interfaz gráfica en Tkinter y al ejecutarlo aparece un menú con las seis opciones, donde cada botón abre la ventana de su proyecto.

Lo más importante es que los códigos originales se unieron sin cambiarlos. La interfaz solo usa las clases que ya teníamos y muestra de forma visual lo que hace cada estructura.

## Los seis proyectos

| # | Proyecto | Estructura de datos | Archivo | Documentación |
|---|----------|---------------------|---------|---------------|
| 1 | Navegador web | Pila | proyectos/p1_navegador_web.py | [Ver documento](docs/1_navegador_pila.md) |
| 2 | Resistencias eléctricas | Arreglos y listas | proyectos/p2_resistencias.py | [Ver documento](docs/2_resistencias_arreglos.md) |
| 3 | Cola de impresión | Cola | proyectos/p3_cola_impresion.py | [Ver documento](docs/3_cola_impresion.md) |
| 4 | Carrito de compras | Listas de objetos | proyectos/p4_carrito_compras.py | [Ver documento](docs/4_carrito_listas.md) |
| 5 | Directorio de alumnos | Árbol binario de búsqueda | proyectos/p5_arbol_alumnos.py | [Ver documento](docs/5_arbol_binario.md) |
| 6 | Ruta Mágica | Grafo y algoritmo de Dijkstra | proyectos/p6_pueblos_magicos.py | [Ver documento](docs/6_grafo_dijkstra.md) |

## Cómo ejecutarlo

Solo se necesita Python 3.8 o una versión más nueva. No hay que instalar nada porque todo lo que se usa viene con Python: `tkinter`, `random`, `heapq`, `dataclasses` y `typing`.

```bash
git clone https://github.com/saimonetii/proyecto-integrador-estructuras-datos.git
cd proyecto-integrador-estructuras-datos

python Main1.py             # menú gráfico
python Main1.py --consola   # menú en la terminal con los programas originales
```

Para abrirlo en VS Code se usa File, Open Folder, se elige la carpeta del proyecto, se abre `Main1.py` y se presiona el botón de ejecutar. Es importante abrir la carpeta completa y no solo el archivo, porque si no el programa no encuentra las carpetas `proyectos` e `interfaz`.

## Cómo está organizado

```
proyecto-integrador-estructuras-datos/
├── Main1.py          ← el único archivo que se ejecuta
├── proyectos/        ← el código de cada proyecto, sin cambios
├── interfaz/         ← una ventana de Tkinter por proyecto
└── docs/             ← la documentación de cada proyecto
```

| Carpeta o archivo | Qué contiene |
|-------------------|--------------|
| Main1.py | El menú principal con las seis opciones y el modo de consola |
| proyectos/ | Los seis códigos con sus clases y su menú de consola, tal como se entregaron. El proyecto 5 se hizo nuevo para el integrador |
| interfaz/ | Las ventanas gráficas de cada proyecto y el archivo estilos.py con los colores y fuentes |
| docs/ | Un documento por proyecto que explica el código |

La idea principal es separar la lógica de la interfaz. Las ventanas no vuelven a programar las estructuras, solo llaman a los métodos que ya existen. Por ejemplo, cuando se presiona el botón Back del navegador, la ventana llama al método `retroceder` de la clase original `NavegadorWeb` y después dibuja cómo quedaron las dos pilas.

## Cómo se unieron los códigos

Al juntar los seis proyectos nos encontramos con algunos detalles que hubo que resolver:

- Los proyectos 1 y 3 tienen una función llamada `menu`, así que si se pegaban en un mismo archivo una borraba a la otra. Por eso cada proyecto se quedó en su propio archivo dentro de `proyectos` y se llama con su nombre.
- El proyecto de Resistencias crea su ventana desde la primera línea del archivo, así que con solo importarlo se abría. Para no modificarlo, `Main1.py` lo ejecuta tal cual en un proceso aparte con `subprocess`.
- Los programas originales usan `input` y `print`, que no sirven dentro de una ventana. Cada ventana lee los datos de cuadros de texto y listas, revisa que sean válidos antes de llamar al método original y muestra los mensajes en una barra de estado.
- Para que nadie se confunda al ejecutarlo, el archivo principal se llama `Main1.py` y el repositorio solo tiene el proyecto integrador.

## Conclusión

Este proyecto junta todo lo que vimos en la materia, desde estructuras lineales como pilas, colas y listas hasta estructuras no lineales como árboles y grafos. Al separar la lógica de la interfaz pudimos respetar los códigos que cada quien entregó y al mismo tiempo mostrar cada estructura de forma visual: se puede ver cómo crece una pila, cómo avanza una cola, cómo se acomoda un árbol y por dónde pasa la ruta más corta en un grafo. Esto hace más fácil explicar cada proyecto y entender por qué cada estructura sirve para el problema que resuelve.

## Fuentes

- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Python Software Foundation. *Data Structures*. https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *subprocess — Subprocess management*. https://docs.python.org/3/library/subprocess.html
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*, 4.ª edición. MIT Press, 2022.

## Integrantes


Universidad Anáhuac Mayab · Estructuras de Datos
