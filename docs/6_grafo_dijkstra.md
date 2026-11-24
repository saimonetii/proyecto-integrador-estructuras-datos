# Ruta Mágica con grafos y el algoritmo de Dijkstra

## Introducción

En este proyecto hicimos un programa que encuentra el camino más corto en kilómetros entre dos Pueblos Mágicos de la Sierra Norte de Puebla. Los pueblos y las carreteras que los unen forman un grafo, y para encontrar la mejor ruta se usa el algoritmo de Dijkstra, que es la misma idea que usan las aplicaciones de mapas como Google Maps o Waze.

## Los grafos y el algoritmo de Dijkstra

Un grafo está formado por vértices y aristas. En este proyecto cada pueblo es un vértice y cada carretera es una arista. El grafo es ponderado porque cada carretera tiene un peso, que son sus kilómetros, y es no dirigido porque cada carretera se puede recorrer en los dos sentidos.

El algoritmo lo creó el científico holandés Edsger W. Dijkstra en 1956 y lo publicó en 1959. Él mismo contó años después que se le ocurrió en una terraza de café mientras estaba de compras con su prometida, sin papel ni lápiz, y que le tomó unos veinte minutos. Su idea es avanzar siempre por el lugar más cercano que todavía no se ha confirmado, y así se garantiza que cuando se llega al destino ya se encontró la ruta más corta.

## Cómo funciona el código

| Concepto | En el proyecto | Clase o atributo |
|----------|----------------|------------------|
| Vértice | Cada pueblo | PuebloMagico, con índice, nombre y clave |
| Arista | Cada carretera | Arista, con destino y distancia |
| Peso | Los kilómetros de la carretera | distancia_km |
| No dirigido | Se puede ir en los dos sentidos | bidireccional=True |

El grafo tiene siete pueblos:

| # | Pueblo | Clave |
|---|--------|-------|
| 1 | Zacatlán de las Manzanas | ZAC |
| 2 | Chignahuapan | CHI |
| 3 | Tetela de Ocampo | TET |
| 4 | Cuetzalan del Progreso | CUE |
| 5 | Tlatlauquitepec | TLA |
| 6 | Xicotepec de Juárez | XIC |
| 7 | Pahuatlán | PAH |

Y diez carreteras:

| Carretera | Kilómetros |
|-----------|------------|
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

El grafo se guarda como una lista de adyacencia, que es un diccionario donde cada pueblo tiene la lista de carreteras que salen de él. Así solo se guarda memoria para las carreteras que existen.

```python
self.adyacencia = {
    "Zacatlan de las Manzanas": [Arista("Chignahuapan", 22), Arista("Tetela de Ocampo", 48), ...],
    "Chignahuapan": [Arista("Zacatlan de las Manzanas", 22), ...],
    ...
}
```

El método `dijkstra` sigue estos pasos:

| Paso | Qué hace | Variable que usa |
|------|----------|------------------|
| 1 | Pone todas las distancias en infinito, menos la del origen, que vale 0 | distancias |
| 2 | Prepara un registro de desde qué pueblo se llegó a cada uno | anteriores |
| 3 | Usa una cola de prioridad que siempre entrega el pueblo más cercano | cola_prioridad con heapq |
| 4 | Saca el pueblo más cercano. Si es un dato viejo lo ignora y si es el destino termina | heappop |
| 5 | Revisa a sus vecinos y, si encuentra un camino más corto hacia alguno, lo actualiza | heappush |
| 6 | Reconstruye la ruta desde el destino hacia atrás y la voltea | camino.reverse() |
| 7 | Arma la lista de tramos con los kilómetros de cada uno | tramos |

## Ejemplo paso a paso

Si se busca la ruta de Pahuatlán a Tlatlauquitepec, hay varias opciones:

| Ruta | Suma | Total |
|------|------|-------|
| Pahuatlán, Zacatlán, Chignahuapan, Tlatlauquitepec | 60 + 22 + 90 | **172 km** |
| Pahuatlán, Xicotepec, Cuetzalan, Tlatlauquitepec | 32 + 115 + 38 | 185 km |
| Pahuatlán, Zacatlán, Tetela, Cuetzalan, Tlatlauquitepec | 60 + 48 + 68 + 38 | 214 km |

El algoritmo regresa la primera, con 172 kilómetros.

## La ventana del proyecto

Se eligen el pueblo de origen y el de destino en dos listas y se presiona Calcular ruta. El grafo se dibuja con un círculo por pueblo y líneas con los kilómetros de cada carretera. La ruta encontrada se pinta de naranja y el origen y el destino de amarillo. A un lado aparece el resultado con la distancia total, los tramos y la ruta completa. La posición de los pueblos en el dibujo es aproximada y solo sirve para que se vea parecido al mapa, el algoritmo no la usa.

## Detalles a tener en cuenta

- Los pueblos y las carreteras están escritos dentro del código, así que para agregar uno nuevo hay que modificar la función `construir_grafo_puebla`. Se podría mejorar leyéndolos desde un archivo.
- Los kilómetros son aproximados para el proyecto.
- Dijkstra solo funciona cuando ningún peso es negativo. Aquí no hay problema porque no existen kilómetros negativos.
- Si hay dos rutas con la misma distancia, el programa muestra solo una.


## Conclusión

Los grafos permiten representar relaciones que no son lineales ni jerárquicas, como un mapa de carreteras donde cada pueblo se conecta con varios. Dijkstra resuelve el problema de la ruta más corta de forma eficiente porque siempre avanza por el pueblo más cercano. Este proyecto junta casi todo lo que vimos en el semestre: listas, diccionarios, una cola de prioridad y un algoritmo clásico aplicado a un problema real de México.

## Fuentes

- Dijkstra, E. W. A note on two problems in connexion with graphs. *Numerische Mathematik*, vol. 1, pp. 269–271, 1959.
- Misa, T. J. y Frana, P. L. An interview with Edsger W. Dijkstra. *Communications of the ACM*, vol. 53, núm. 8, pp. 41–47, 2010.
- Python Software Foundation. *heapq — Heap queue algorithm*. https://docs.python.org/3/library/heapq.html
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. y Stein, C. *Introduction to Algorithms*, 4.ª edición, capítulo 22. MIT Press, 2022.
- Secretaría de Turismo. *Pueblos Mágicos*. https://www.gob.mx/sectur
