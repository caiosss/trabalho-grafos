class Estado():
    def __init__(self, nome, vizinhos):
        self.nome = nome
        self.vizinhos = vizinhos

    def possui_vizinho(self, vizinho):
        return vizinho in self.vizinhos