import numpy as np
import matplotlib.pyplot as plt
import estados


np.set_printoptions(threshold=np.inf, linewidth=np.inf)
matriz_incidencia = np.zeros((len(estados.estados), len(estados.arestas)), dtype=int)

for i, estado in enumerate(estados.estados):
    for j, (estado1, estado2) in enumerate(estados.arestas):
        if estado.nome == estado1 or estado.nome == estado2:
            matriz_incidencia[i][j] = 1
print(matriz_incidencia)

plt.imshow(matriz_incidencia, cmap="Blues")
plt.xticks(range(len(estados.arestas)), [f"{estado1}-{estado2}" for estado1, estado2 in estados.arestas], rotation=90)
plt.yticks(range(len(estados.estados)), [estado.nome for estado in estados.estados])
plt.title("Matriz de incidência")
plt.show()