"""Colores, fuentes y pequeños ayudantes de Tkinter compartidos por todas las ventanas.

Estilo clásico de Tkinter (fondo gris, botones normales, recuadros con título),
parecido a la ventana del proyecto de Resistencias. Tenerlo en un solo lugar
hace que las ventanas se vean iguales y que un cambio se haga solo aquí.
"""

import tkinter as tk

# ----------------------------------------------------------------- COLORES
FONDO = "#F0F0F0"          # gris clásico de las ventanas de Windows
TARJETA = "#F0F0F0"        # fondo de los recuadros (igual que la ventana)
BORDE = "#A0A0A0"
TEXTO = "#000000"
TEXTO_SUAVE = "#555555"
PRIMARIO = "#0000AA"
EXITO = "#006400"
PELIGRO = "#B00000"
RESALTE = "#FFFF00"        # amarillo para resaltar (tope, nodo encontrado, ruta...)

# Un color por proyecto (se usa en el título de cada ventana y en los dibujos)
COLOR_PROYECTO = {
    1: "#0000FF",  # Navegador - Pila
    2: "#8B4513",  # Resistencias - Arreglos
    3: "#008000",  # Cola de impresión - Cola
    4: "#FF0000",  # Carrito - Listas
    5: "#800080",  # Árbol binario
    6: "#FF8C00",  # Pueblos Mágicos - Grafo
}

# ----------------------------------------------------------------- FUENTES
FUENTE = "Segoe UI"
F_TITULO = (FUENTE, 12, "bold")
F_SUBTITULO = (FUENTE, 10, "bold")
F_NORMAL = (FUENTE, 9)
F_NEGRITA = (FUENTE, 9, "bold")
F_PEQUENA = (FUENTE, 8)
F_MONO = ("Consolas", 9)


def configurar_ttk(raiz: tk.Misc) -> None:
    """Se deja el tema de ttk que trae el sistema (el normal de Windows)."""
    return None


def encabezado(ventana: tk.Misc, numero: int, titulo: str, estructura: str) -> tk.Frame:
    """Título sencillo con el número, nombre del proyecto y la estructura usada."""
    barra = tk.Frame(ventana, bg=FONDO, padx=10, pady=6)
    barra.pack(fill="x")
    tk.Label(barra, text=f"Proyecto {numero}: {titulo}", font=F_TITULO,
             bg=FONDO, fg=COLOR_PROYECTO[numero]).pack()
    tk.Label(barra, text=f"Estructura de datos: {estructura}", font=F_NORMAL,
             bg=FONDO, fg=TEXTO).pack()
    return barra


def boton(padre: tk.Misc, texto: str, comando, color: str = None, **kwargs) -> tk.Button:
    """Botón normal de Tkinter (el parámetro color se ignora para mantener el estilo clásico)."""
    return tk.Button(padre, text=texto, command=comando, font=F_NORMAL, padx=6, **kwargs)


def panel(padre: tk.Misc, titulo: str = "") -> tk.LabelFrame:
    """Recuadro clásico con título (LabelFrame)."""
    return tk.LabelFrame(padre, text=titulo, font=F_NORMAL, bg=TARJETA, padx=8, pady=6)


def barra_estado(ventana: tk.Misc) -> tk.Label:
    """Etiqueta inferior donde cada ventana escribe lo que acaba de pasar."""
    etiqueta = tk.Label(ventana, text="Listo.", anchor="w", font=F_NORMAL,
                        bg=FONDO, fg=TEXTO, relief="sunken", bd=1, padx=6, pady=2)
    etiqueta.pack(fill="x", side="bottom")
    return etiqueta


def mensaje(etiqueta: tk.Label, texto: str, tipo: str = "info") -> None:
    """Escribe un mensaje en la barra de estado con color según el tipo."""
    colores = {"info": TEXTO, "ok": EXITO, "error": PELIGRO}
    etiqueta.config(text=texto, fg=colores.get(tipo, TEXTO))
