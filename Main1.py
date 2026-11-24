"""PROYECTO INTEGRADOR DE ESTRUCTURAS DE DATOS

Este es el ÚNICO archivo que hay que ejecutar. Abre un menú gráfico con los
6 proyectos de la materia; cada botón abre la ventana de ese proyecto:

    1. Navegador web ............ Pilas (LIFO)
    2. Resistencias eléctricas .. Arreglos / tuplas y listas (ya traía Tkinter)
    3. Cola de impresión ........ Colas (FIFO) de capacidad limitada
    4. Carrito de compras ....... Listas de objetos y búsqueda
    5. Directorio de alumnos .... Árbol binario de búsqueda
    6. Ruta Mágica .............. Grafos ponderados + Dijkstra

Uso:
    python Main1.py            -> menú gráfico (Tkinter)
    python Main1.py --consola  -> menú en la terminal que corre los programas
                                 originales tal cual (con input/print)

El código de cada proyecto está en la carpeta `proyectos/` SIN CAMBIOS, y las
ventanas gráficas están en la carpeta `interfaz/` (solo usan esas clases).
"""

import subprocess
import sys
import tkinter as tk
from pathlib import Path

from interfaz import estilos as e

CARPETA_PROYECTOS = Path(__file__).resolve().parent / "proyectos"

# (número, título, estructura, descripción corta)
PROYECTOS = [
    (1, "Navegador web", "Pila (LIFO)",
     "Historial con botones Back y Forward usando dos pilas."),
    (2, "Resistencias eléctricas", "Arreglos y listas",
     "Bandas de color de una resistencia y suma en serie y en paralelo."),
    (3, "Cola de impresión", "Cola (FIFO)",
     "5 computadoras mandan trabajos a una impresora con capacidad de 6."),
    (4, "Carrito de compras", "Listas de objetos",
     "Catálogo, búsqueda por ID o nombre, carrito y total a pagar."),
    (5, "Directorio de alumnos", "Árbol binario de búsqueda",
     "Insertar, buscar y eliminar alumnos por matrícula y ver recorridos."),
    (6, "Ruta Mágica", "Grafo + Dijkstra",
     "Camino más corto entre Pueblos Mágicos de Puebla."),
]


# =============================================================== MODO GRÁFICO
class MenuPrincipal:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Proyecto Integrador - Estructuras de Datos")
        self.raiz.geometry("520x420")
        self.raiz.configure(bg=e.FONDO)
        e.configurar_ttk(self.raiz)

        self.ventanas = {}           # número de proyecto -> ventana abierta
        self.proceso_resistencias = None

        tk.Label(self.raiz, text="Proyecto Integrador de Estructuras de Datos",
                 font=e.F_TITULO, bg=e.FONDO).pack(pady=(12, 2))
        tk.Label(self.raiz, text="Selecciona un proyecto:", font=e.F_NORMAL,
                 bg=e.FONDO).pack(pady=(0, 8))

        # Un botón por proyecto, uno debajo del otro
        marco = tk.Frame(self.raiz, bg=e.FONDO)
        marco.pack()
        for numero, titulo, estructura, descripcion in PROYECTOS:
            tk.Button(marco, text=f"{numero}. {titulo}", width=28, font=e.F_NORMAL,
                      fg=e.COLOR_PROYECTO[numero],
                      command=lambda n=numero: self.abrir(n)).grid(
                row=numero - 1, column=0, padx=5, pady=4, sticky="w")
            tk.Label(marco, text=estructura, font=e.F_NORMAL, bg=e.FONDO,
                     anchor="w").grid(row=numero - 1, column=1, padx=5, sticky="w")

        tk.Label(self.raiz, text="Tip: con  python Main1.py --consola  se corren\n"
                                 "las versiones originales en la terminal.",
                 font=e.F_PEQUENA, bg=e.FONDO, fg=e.TEXTO_SUAVE).pack(pady=(14, 6))
        tk.Button(self.raiz, text="Salir", width=10, font=e.F_NORMAL,
                  command=self.raiz.destroy).pack(pady=6)

    def abrir(self, numero):
        # El proyecto 2 ya era una ventana Tkinter completa: se ejecuta su
        # archivo original tal cual, en su propio proceso.
        if numero == 2:
            if self.proceso_resistencias is None or self.proceso_resistencias.poll() is not None:
                self.proceso_resistencias = subprocess.Popen(
                    [sys.executable, str(CARPETA_PROYECTOS / "p2_resistencias.py")])
            return

        # Si la ventana ya está abierta, solo se trae al frente
        abierta = self.ventanas.get(numero)
        if abierta is not None and abierta.ventana.winfo_exists():
            abierta.ventana.deiconify()
            abierta.ventana.lift()
            abierta.ventana.focus_force()
            return

        # Se importan aquí para que el menú abra rápido
        if numero == 1:
            from interfaz.ventana_navegador import VentanaNavegador as Ventana
        elif numero == 3:
            from interfaz.ventana_cola import VentanaCola as Ventana
        elif numero == 4:
            from interfaz.ventana_carrito import VentanaCarrito as Ventana
        elif numero == 5:
            from interfaz.ventana_arbol import VentanaArbol as Ventana
        else:
            from interfaz.ventana_pueblos import VentanaPueblos as Ventana
        self.ventanas[numero] = Ventana(self.raiz)

    def ejecutar(self):
        self.raiz.mainloop()


# ================================================================ MODO CONSOLA
def menu_consola():
    """Corre los programas ORIGINALES en la terminal, tal como fueron entregados."""
    from proyectos import p1_navegador_web, p3_cola_impresion, p5_arbol_alumnos
    from proyectos.p4_carrito_compras import SistemaCarrito
    from proyectos.p6_pueblos_magicos import RutaMagicaApp, construir_grafo_puebla

    while True:
        print("\n=== PROYECTO INTEGRADOR DE ESTRUCTURAS DE DATOS ===")
        for numero, titulo, estructura, _ in PROYECTOS:
            print(f"{numero}. {titulo} ({estructura})")
        print("0. Salir")
        opcion = input("Selecciona un proyecto: ").strip()

        if opcion == "1":
            p1_navegador_web.menu()
        elif opcion == "2":
            print("Abriendo la ventana de Resistencias... ciérrala para volver al menú.")
            subprocess.run([sys.executable, str(CARPETA_PROYECTOS / "p2_resistencias.py")])
        elif opcion == "3":
            p3_cola_impresion.menu()
        elif opcion == "4":
            SistemaCarrito().ejecutar()
        elif opcion == "5":
            p5_arbol_alumnos.menu()
        elif opcion == "6":
            RutaMagicaApp(construir_grafo_puebla()).ejecutar()
        elif opcion == "0":
            print("Cerrando la aplicación. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    if "--consola" in sys.argv:
        menu_consola()
    else:
        MenuPrincipal().ejecutar()
