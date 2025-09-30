Karen Esmeralda Portillo Portillo SMSS202223


Yolanda Isabel Marroquín Ulloa SMSS047424

Interpretación de resultados
a. Describe brevemente de qué trata el dataset utilizado
El dataset contiene 50 registros con 5 columnas: Unnamed:0 (índice o identificador), y cuatro variables numéricas (A, B, C, D). Estas parecen ser datos generados de manera aleatoria o simulada, posiblemente con una distribución normal, útiles para practicar análisis estadístico.

b. ¿Qué información permite ver el resumen estadístico?
El describe() muestra:
count: número de registros (50 en cada columna).
mean: promedio de los valores.
std: dispersión o variabilidad de los datos.
min y max: valores extremos.
25%, 50%, 75%: los cuartiles, que dividen la distribución en partes.
Esto permite conocer el rango de los datos, su tendencia central y dispersión.

c. ¿Qué cambios o tendencias se detectan en la información del dataset?
Las columnas A, B, C y D tienen medias cercanas a 0, lo que indica simetría alrededor del cero (propio de datos distribuidos normalmente).
Sin embargo, hay bastante variabilidad (ejemplo: columna A tiene valores entre -2.08 y 2.76).
La columna B muestra una media negativa (-0.12), pero con una mediana cercana a 0 → tendencia ligeramente sesgada a la izquierda.

d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?
En los datos ordenados:
La columna A muestra casos extremos: un valor mínimo (-2.08) y máximo (2.76) que destacan.
En la columna B, hay un valor máximo muy alto (2.63) que contrasta con su media negativa.
Sobresalen porque son outliers (valores atípicos), que influyen en la variabilidad y pueden deberse a la forma en que se generaron los datos.

e. ¿Qué diferencias se observan entre los primeros y últimos registros?
En las primeras filas (índices 0–4) se ven valores de A más negativos y un caso extremo en B (2.63 en el índice 2).
En las últimas filas (45–49) hay valores más moderados, aunque también aparecen negativos fuertes en B (-1.88).
En general, los primeros registros muestran mayor variabilidad, mientras que los últimos son más estables en torno a valores pequeños.

f. ¿Qué aportan las medidas estadísticas al análisis del dataset?
Media y mediana: resumen la tendencia central.
Desviación estándar: mide cuánto se dispersan los datos respecto al promedio.
Mínimos, máximos y cuartiles: muestran los rangos y ayudan a detectar outliers.
Comparaciones entre columnas: permiten identificar cuál variable es más estable, cuál tiene más dispersión y si hay sesgos.

