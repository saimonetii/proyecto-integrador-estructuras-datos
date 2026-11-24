# Proyecto Integrador de Estructuras de Datos

## Introducción

Hablaremos del proyecto integrador de la materia de Estructuras de Datos. Durante el semestre hicimos seis proyectos, cada uno enfocado en una estructura distinta: pilas, arreglos, colas, listas, árboles y grafos. El objetivo de este proyecto final fue juntar los seis en **un solo programa en Python con interfaz gráfica (Tkinter)**: al ejecutarlo aparece un menú con las seis opciones y cada una abre la ventana de su proyecto.

Lo más importante es que los códigos originales se integraron **sin cambiarlos**: la interfaz solo usa las clases que ya teníamos y las muestra de forma visual.

## Origen

Cada proyecto se entregó por separado, como un programa de consola con su propio menú, salvo el de Resistencias, que ya tenía ventana con Tkinter. Al final del semestre teníamos seis archivos distintos que se ejecutaban cada uno por su lado, y la idea del integrador fue unirlos en una sola aplicación, documentarla y subirla a GitHub para poder exponerla y explicar el código.

## Los 6 proyectos

| # | Proyecto | Estructura de datos | Archivo | Documentación |
|---|----------|---------------------|---------|---------------|
| 1 | Navegador web (Back / Forward) | Pila (LIFO) | `proyectos/p1_navegador_web.py` | [docs/1_navegador_pila.md](docs/1_navegador_pila.md) |
| 2 | Resistencias eléctricas | Arreglos, tuplas y listas | `proyectos/p2_resistencias.py` | [docs/2_resistencias_arreglos.md](docs/2_resistencias_arreglos.md) |
| 3 | Cola de impresión | Cola (FIFO) con capacidad limitada | `proyectos/p3_cola_impresion.py` | [docs/3_cola_impresion.md](docs/3_cola_impresion.md) |
| 4 | Carrito de compras | Listas de objetos y búsqueda | `proyectos/p4_carrito_compras.py` | [docs/4_carrito_listas.md](docs/4_carrito_listas.md) |
| 5 | Directorio de alumnos | Árbol binario de búsqueda | `proyectos/p5_arbol_alumnos.py` | [docs/5_arbol_binario.md](docs/5_arbol_binario.md) |
| 6 | Ruta Mágica (Pueblos Mágicos de Puebla) | Grafo ponderado + Dijkstra | `proyectos/p6_pueblos_magicos.py` | [docs/6_grafo_dijkstra.md](docs/6_grafo_dijkstra.md) |

Cada documento de `docs/` sigue la misma estructura: introducción, origen, funcionamiento, problemas, solución, forecast, conclusión y fuentes.

## Cómo ejecutarlo

**Requisitos:** Python 3.8 o más nuevo. No hay que instalar nada, porque solo se usa la biblioteca estándar (`tkinter`, `random`, `heapq`, `dataclasses`, `typing`).

```bash
git clone https://github.com/saimonetii/proyecto-integrador-estructuras-datos.git
cd proyecto-integrador-estructuras-datos

python Main1.py             # menú gráfico
python Main1.py --consola   # menú en la terminal con los programas originales
```

**En VS Code:** File → Open Folder, se elige la carpeta del proyecto, se abre `Main1.py` y se presiona ▶. Hay que abrir la carpeta completa para que encuentre `proyectos/` e `interfaz/`.

## Organización del código

```
proyecto-integrador-estructuras-datos/
├── Main1.py          ← el único que se ejecuta: menú con las 6 opciones
├── proyectos/        ← el código de cada proyecto, sin cambios
├── interfaz/         ← una ventana de Tkinter por proyecto + estilos.py
└── docs/             ← documentación de cada proyecto
```

| Parte | Qué contiene | ¿Se modificó? |
|-------|--------------|---------------|
| `proyectos/` | Las clases de cada estructura (Pila, ColaImpresion, Carrito, ArbolBinarioBusqueda, GrafoPueblosMagicos…) y su menú de consola | No. Son los códigos entregados; el 5 es nuevo |
| `interfaz/` | Las ventanas: botones, tablas y dibujos con `Canvas` | Código nuevo |
| `Main1.py` | El menú principal y el modo `--consola` | Código nuevo |

Las ventanas solo **llaman a los métodos originales**. Por ejemplo, el botón *Back* del navegador hace `self.navegador.retroceder()`, y el dibujo de las pilas se hace leyendo `pila_atras.elementos`. A esto se le llama separar la lógica de la presentación.

## Problemas

Al juntar los seis códigos aparecieron varios problemas:

| Problema | Por qué pasaba |
|----------|----------------|
| No se podían pegar todos en un solo archivo | Los proyectos 1 y 3 tienen una función llamada `menu()` y una pisaba a la otra |
| El proyecto 2 se abría solo | `p2_resistencias.py` crea su ventana (`tk.Tk()`) desde el inicio del archivo, así que con solo importarlo ya se abría |
| Los programas usaban `input()` y `print()` | En una ventana gráfica no hay consola para escribir ni leer |
| Confusión con dos archivos `main.py` | En una prueba se ejecutó el `main.py` viejo y solo salía el proyecto de Resistencias |

## Solución

| Problema | Solución |
|----------|----------|
| Nombres repetidos | Cada proyecto se quedó en su propio archivo dentro de `proyectos/` y se importa con su nombre (`p1_navegador_web.menu()`, `p3_cola_impresion.menu()`) |
| Proyecto 2 | `Main1.py` ejecuta su archivo original en un proceso aparte con `subprocess`, sin tocarlo |
| `input()` y `print()` | Cada ventana lee los datos de cuadros de texto y listas, valida antes de llamar al método original y muestra los mensajes en una barra de estado |
| Dos `main.py` | El archivo principal se llama `Main1.py` y el repositorio solo contiene el proyecto integrador |

## Forecast

- **Optimista:** como cada ventana es independiente, agregar un séptimo proyecto solo requiere su archivo en `proyectos/`, su ventana en `interfaz/` y una línea en la lista `PROYECTOS` de `Main1.py`.
- **Probable:** el programa se usa para la exposición y como material de estudio; cada integrante puede abrir su proyecto original y explicarlo igual que como lo entregó.
- **Pesimista:** si en otra computadora no está instalado Tkinter (pasa en algunas versiones de Linux), las ventanas no abren. En ese caso se puede usar `python Main1.py --consola`, que no necesita interfaz gráfica, o instalarlo con `sudo apt install python3-tk`.

## Conclusión

El proyecto integrador junta en un solo programa todo lo que vimos en la materia, desde estructuras lineales como pilas, colas y listas hasta estructuras no lineales como árboles y grafos. Al separar la lógica de la interfaz pudimos respetar los códigos originales y al mismo tiempo mostrar cada estructura de forma visual: se ve cómo crece una pila, cómo avanza una cola, cómo se ordena un árbol y por dónde pasa la ruta más corta en un grafo. Esto facilita explicar cada proyecto y entender por qué cada estructura sirve para el problema que resuelve.

## Fuentes

- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Python Software Foundation. *Data Structures* (listas, pilas y colas). https://docs.python.org/3/tutorial/datastructures.html
- Python Software Foundation. *subprocess — Subprocess management*. https://docs.python.org/3/library/subprocess.html
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. (2022). *Introduction to Algorithms* (4.ª ed.). MIT Press.

## Integrantes

- Samuel Coronado
- *(agregar a los demás integrantes del equipo)*

Universidad Anáhuac Mayab · Estructuras de Datos
