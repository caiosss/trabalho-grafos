import estados
import matplotlib.pyplot as plt

class ListaIndexada:
    def __init__(self, estados):
        self.estados = estados
        self.alfas = {}
        self.betas = []
        self.construir_listas()

    def construir_listas(self):
        index = 0
        for i, estado in enumerate(self.estados):
            self.alfas[estado.nome] = index
            self.betas.extend(estado.vizinhos)
            index = len(self.betas)

    def contar_vizinhos(self):
        return {estados:
                    self.betas[self.alfas[estados]:
                               self.alfas[estados] + self.betas[self.alfas[estados]:]
                               .count(estados)].__len__()
                for estados in self.alfas.keys()}

    def mostrar_listas(self):
        print("Lista alfa: ")
        print("{" + ", ".join(f'\"{estado}\": {indice}' for estado, indice in self.alfas.items()) + "}")

        print("\nLista beta: ")
        print(self.betas)

    def plotar_histograma(self):
        contagem_vizinhos = {estado: self.betas.count(estado) for estado in self.alfas.keys()}

        estados = list(contagem_vizinhos.keys())
        vizinhos = list(contagem_vizinhos.values())

        plt.figure(figsize=(12, 6))
        plt.bar(estados, vizinhos, color="purple")

        plt.xlabel("Estados")
        plt.ylabel("Quantidade de vizinhos")
        plt.title("Quantidade de vizinhos por estado")
        plt.xticks(rotation=90)
        plt.grid(axis="y", linestyle="--", linewidth=0.7)

        plt.show()

grafo = ListaIndexada(estados.estados)
grafo.mostrar_listas()
grafo.plotar_histograma()