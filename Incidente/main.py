import numpy as np
import estados


np.set_printoptions(threshold=np.inf, linewidth=np.inf)
matriz_incidencia = np.zeros((len(estados.estados), len(estados.arestas)), dtype=int)

for i, estado in enumerate(estados.estados):
    for j, (estado1, estado2) in enumerate(estados.arestas):
        if estado.nome == estado1 or estado.nome == estado2:
            matriz_incidencia[i][j] = 1
print(estados.arestas)
print(matriz_incidencia)