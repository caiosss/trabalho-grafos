import estados
import matplotlib.pyplot as plt
import numpy as np
matriz = np.zeros((len(estados.estados), len(estados.estados)), dtype=int)

for i in range(len(estados.estados)):
    for j in range(len(estados.estados)):
        if estados.estados[i].nome in estados.estados[j].vizinhos:
            matriz[i][j] = 1
print(matriz)


