# O grafo (mapa de conexões com pesos/custos)
grafo = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}

# Tabela de custos para cada nó
custos = {
    "a": 6,
    "b": 2,
    "fim": float("inf")
}

# Tabela de "pais" para reconstruir o caminho
pais = {
    "a": "inicio",
    "b": "inicio",
    "fim": None
}

# Lista para manter o controle dos nós já processados
processados = []


def ache_no_custo_mais_baixo(custos_locais):
    """
    Encontra o nó com o menor custo que ainda não foi processado.
    """
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos_locais:
        custo_atual = custos_locais[nodo]
        # Correção do bug: compara o custo_atual, não o dicionário inteiro
        if custo_atual < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo_atual
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


def dijkstra():
    """
    Executa o algoritmo de Dijkstra para encontrar o caminho mais barato.
    """
    # Encontra o nó inicial a ser processado
    nodo = ache_no_custo_mais_baixo(custos)

    # Loop principal do algoritmo
    while nodo is not None:
        custo_do_nodo = custos[nodo]
        vizinhos = grafo[nodo]
        for n in vizinhos.keys():
            novo_custo = custo_do_nodo + vizinhos[n]
            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = nodo
        # Marca o nó como processado
        processados.append(nodo)
        # Encontra o próximo nó a ser processado
        nodo = ache_no_custo_mais_baixo(custos)


if __name__ == "__main__":
    dijkstra()
    print("Custo do início para cada nó:")
    print(custos)
    print("Caminho mais barato encontrado tem o custo de:", custos["fim"])
