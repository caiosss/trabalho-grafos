import estado
estados = [
    estado.Estado("Ceará", ["Piauí", "Pernambuco", "Paraíba", "Rio Grande do Norte"]),
    estado.Estado("Piauí", ["Ceará", "Maranhão", "Tocantins", "Pernambuco", "Bahia"]),
    estado.Estado("Pernambuco", ["Ceará", "Paraíba", "Bahia", "Piauí", "Alagoas"]),
    estado.Estado("Paraíba", ["Ceará", "Pernambuco", "Rio Grande do Norte"]),
    estado.Estado("Rio Grande do Norte", ["Ceará", "Paraíba"]),
    estado.Estado("Maranhão", ["Piauí", "Tocantins", "Pará"]),
    estado.Estado("Tocantins", ["Maranhão", "Piauí", "Pará", "Goiás", "Mato Grosso", "Bahia"]),
    estado.Estado("Bahia", ["Piauí", "Pernambuco", "Minas Gerais", "Espírito Santo", "Sergipe", "Alagoas", "Goiás", "Tocantins"]),
    estado.Estado("Alagoas", ["Pernambuco", "Bahia", "Sergipe"]),
    estado.Estado("Sergipe", ["Alagoas", "Bahia"]),
    estado.Estado("Pará", ["Maranhão", "Tocantins", "Amapá", "Amazonas", "Roraima", "Mato Grosso"]),
    estado.Estado("Goiás", ["Tocantins", "Bahia", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Distrito Federal"]),
    estado.Estado("Mato Grosso", ["Tocantins", "Pará", "Rondônia", "Amazonas", "Mato Grosso do Sul", "Goiás"]),
    estado.Estado("Mato Grosso do Sul", ["Mato Grosso", "Goiás", "Paraná", "São Paulo", "Minas Gerais"]),
    estado.Estado("Distrito Federal", ["Goiás", "Minas Gerais"]),
    estado.Estado("Minas Gerais", ["Bahia", "Goiás", "Mato Grosso do Sul", "São Paulo", "Rio de Janeiro", "Espírito Santo",
                            "Distrito Federal"]),
    estado.Estado("Espírito Santo", ["Bahia", "Minas Gerais", "Rio de Janeiro"]),
    estado.Estado("Rio de Janeiro", ["Minas Gerais", "Espírito Santo", "São Paulo"]),
    estado.Estado("São Paulo", ["Rio de Janeiro", "Minas Gerais", "Mato Grosso do Sul", "Paraná"]),
    estado.Estado("Paraná", ["São Paulo", "Santa Catarina", "Mato Grosso do Sul"]),
    estado.Estado("Santa Catarina", ["Paraná", "Rio Grande do Sul"]),
    estado.Estado("Rio Grande do Sul", ["Santa Catarina"]),
    estado.Estado("Acre", ["Amazonas", "Rondônia"]),
    estado.Estado("Amazonas", ["Pará", "Roraima", "Acre", "Rondônia", "Mato Grosso"]),
    estado.Estado("Roraima", ["Amazonas", "Pará"]),
    estado.Estado("Rondônia", ["Acre", "Amazonas", "Mato Grosso"]),
    estado.Estado("Amapá", ["Pará"]),
]
arestas = list()
for estado in estados:
    for vizinho in estado.vizinhos:
        if (estado.nome, vizinho) not in arestas and (vizinho, estado.nome) not in arestas:
            arestas.append((estado.nome, vizinho))