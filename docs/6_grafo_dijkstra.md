# Proyecto 6: Ruta Mágica con Grafos y Dijkstra

[← Volver al README](../README.md) · Código: [`proyectos/p6_pueblos_magicos.py`](../proyectos/p6_pueblos_magicos.py) · Ventana: [`interfaz/ventana_pueblos.py`](../interfaz/ventana_pueblos.py)

## Introducción

Hablaremos del sexto proyecto: un programa que encuentra el **camino más corto en kilómetros** entre dos Pueblos Mágicos de la Sierra Norte de **Puebla**. Los pueblos y las carreteras que los unen forman un **grafo**, y para encontrar la mejor ruta se usa el **algoritmo de Dijkstra**, el mismo principio que usan las aplicaciones de mapas como Google Maps o Waze.

## Origen

Edsger W. Dijkstra, científico holandés, ideó el algoritmo en **1956** mientras trabajaba en el Centro Matemático de Ámsterdam y lo publicó en **1959**. En una entrevista de 2001 contó que se le ocurrió en una terraza de café mientras estaba de compras con su prometida, sin papel ni lápiz, y lo llamó "un invento de veinte minutos". Por otro lado, los Pueblos Mágicos son un programa de la Secretaría de Turismo de México que reconoce a pueblos con atractivos culturales e históricos, y Puebla tiene varios en la Sierra Norte, como Zacatlán, Chignahuapan y Cuetzalan.

## Funcionamiento

### El grafo

| Concepto | En el proyecto | Clase |
|----------|----------------|-------|
| Vértice (nodo) | Cada pueblo | `PuebloMagico` (índice, nombre, clave como `ZAC`) |
| Arista | Cada carretera | `Arista` (destino y `distancia_km`) |
| Peso | Los kilómetros de cada carretera | `distancia_km` |
| No dirigido | Se puede ir en los dos sentidos | `agregar_carretera(..., bidireccional=True)` |

### Pueblos (7 vértices)

| # | Pueblo | Clave |
|---|--------|-------|
| 1 | Zacatlán de las Manzanas | ZAC |
| 2 | Chignahuapan | CHI |
| 3 | Tetela de Ocampo | TET |
| 4 | Cuetzalan del Progreso | CUE |
| 5 | Tlatlauquitepec | TLA |
| 6 | Xicotepec de Juárez | XIC |
| 7 | Pahuatlán | PAH |

### Carreteras (10 aristas)

| Carretera | km |
|-----------|----|
| Zacatlán – Chignahuapan | 22 |
| Zacatlán – Tetela de Ocampo | 48 |
| Chignahuapan – Tetela de Ocampo | 42 |
| Tetela de Ocampo – Cuetzalan | 68 |
| Cuetzalan – Tlatlauquitepec | 38 |
| Zacatlán – Xicotepec | 55 |
| Xicotepec – Pahuatlán | 32 |
| Pahuatlán – Zacatlán | 60 |
| Chignahuapan – Tlatlauquitepec | 90 |
| Xicotepec – Cuetzalan | 115 |

### Lista de adyacencia

El grafo se guarda como un **diccionario** donde cada pueblo tiene la lista de carreteras que salen de él. Así solo se guarda memoria para las carreteras que existen, a diferencia de una matriz de adyacencia de 7 × 7.

```python
self.adyacencia = {
    "Zacatlan de las Manzanas": [Arista("Chignahuapan", 22), Arista("Tetela de Ocampo", 48), ...],
    "Chignahuapan": [Arista("Zacatlan de las Manzanas", 22), ...],
    ...
}
```

### Algoritmo de Dijkstra paso a paso

| Paso | Qué hace | Variable |
|------|----------|----------|
| 1 | Todas las distancias empiezan en infinito, menos el origen, que vale 0 | `distancias` |
| 2 | Se guarda de qué pueblo se llegó a cada uno | `anteriores` |
| 3 | Un **montículo mínimo** siempre entrega el pueblo más cercano que falta | `cola_prioridad` (`heapq`) |
| 4 | Se saca el más cercano; si es un dato viejo se ignora (`continue`) y si es el destino se termina (`break`) | `heappop` |
| 5 | Para cada vecino, si `distancia_actual + km` es mejor que la guardada, se actualiza ("relajar" la arista) | `heappush` |
| 6 | Se reconstruye el camino desde el destino hacia atrás con `anteriores` y se invierte | `camino.reverse()` |
| 7 | Se arman los tramos `(origen, destino, km)` para mostrarlos | `tramos` |

### Ejemplo: Pahuatlán → Tlatlauquitepec

| Ruta posible | Cálculo | Total |
|--------------|---------|-------|
| **Pahuatlán → Zacatlán → Chignahuapan → Tlatlauquitepec** | 60 + 22 + 90 | **172 km** ✅ |
| Pahuatlán → Xicotepec → Cuetzalan → Tlatlauquitepec | 32 + 115 + 38 | 185 km |
| Pahuatlán → Zacatlán → Tetela → Cuetzalan → Tlatlauquitepec | 60 + 48 + 68 + 38 | 214 km |

Dijkstra regresa la ruta de **172 km**.

### En la interfaz

Se eligen el origen y el destino en listas desplegables y se presiona **Calcular ruta (Dijkstra)**. El grafo se dibuja con círculos para los pueblos y líneas con los kilómetros, la ruta encontrada se pinta en naranja y el origen y el destino en amarillo. El panel de resultado muestra la distancia total, los tramos y la ruta completa. La posición de los pueblos en el dibujo es aproximada y solo sirve para dibujar; el algoritmo no la usa.

## Problemas

| Problema | Explicación |
|----------|-------------|
| El grafo está fijo en el código | Para agregar un pueblo o carretera hay que modificar `construir_grafo_puebla()` |
| Distancias aproximadas | Los kilómetros son aproximados para el proyecto, no medidos sobre carretera real |
| No sirve con pesos negativos | Dijkstra supone que ningún tramo "resta" distancia |
| Empates | Si hay dos rutas con la misma distancia, solo se muestra una |

## Solución

| Problema | Solución |
|----------|----------|
| Grafo fijo | Leer los pueblos y carreteras desde un archivo (CSV o JSON) para poder cambiarlos sin tocar el código |
| Distancias | Se podrían obtener de una fuente oficial o de un servicio de mapas |
| Pesos negativos | No aplica: no existen kilómetros negativos. Para grafos con pesos negativos existe el algoritmo de Bellman-Ford |
| Empates | Para este proyecto basta con una ruta; se podría guardar una lista de anteriores para mostrar todas |

## Forecast

- **Optimista:** el destino está conectado directamente al origen y el algoritmo termina en pocos pasos gracias al `break`.
- **Probable:** el algoritmo revisa parte del grafo antes de llegar al destino; su costo es O((V + E) log V), donde V son los pueblos y E las carreteras.
- **Pesimista:** no existe ruta entre los dos pueblos y el algoritmo revisa todo lo que puede alcanzar antes de decir "No existe ruta conectada entre esos pueblos".

## Conclusión

Los grafos permiten representar relaciones que no son lineales ni jerárquicas, como un mapa de carreteras donde cualquier pueblo puede conectarse con varios. Dijkstra resuelve el problema de la ruta más corta de forma eficiente porque siempre avanza por el pueblo más cercano, y gracias al montículo (`heapq`) encuentra ese pueblo en O(log V). Este proyecto junta casi todo lo que vimos en el semestre: listas, diccionarios, una cola de prioridad y un algoritmo clásico aplicado a un problema real.

## Fuentes

- Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. *Numerische Mathematik, 1*, 269–271.
- Misa, T. J. y Frana, P. L. (2010). An interview with Edsger W. Dijkstra. *Communications of the ACM, 53*(8), 41–47.
- Python Software Foundation. *heapq — Heap queue algorithm*. https://docs.python.org/3/library/heapq.html
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. (2022). *Introduction to Algorithms* (4.ª ed.), cap. 22 "Single-Source Shortest Paths". MIT Press.
- Secretaría de Turismo. *Pueblos Mágicos*. https://www.gob.mx/sectur
