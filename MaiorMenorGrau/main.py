import estados
import matplotlib.pyplot as plt

def pegarVerticeMaior(grafo):
    maior = 0
    vertice = ""
    vizinhos = []
    for estado in grafo:
        if len(estado.vizinhos) > maior:
            maior = len(estado.vizinhos)
            vertice = estado.nome
            vizinhos = estado.vizinhos
    return"Maior grau: "+ vertice +": "+ vizinhos.__str__()

def pegarVerticeMenor(grafo):
    menor = 100
    vertice = ""
    vizinhos = []
    for estado in grafo:
        if len(estado.vizinhos) < menor:
            menor = len(estado.vizinhos)
            vertice = estado.nome
            vizinhos = estado.vizinhos
    return "Menor grau: " + vertice + ": " + vizinhos.__str__()

print(pegarVerticeMaior(estados.estados))
print(pegarVerticeMenor(estados.estados))