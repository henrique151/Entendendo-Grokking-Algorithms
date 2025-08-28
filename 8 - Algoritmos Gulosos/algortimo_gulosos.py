def aproximacao_gulosa():
    """
    Resolve o Problema da Cobertura de Conjuntos usando um algoritmo guloso.
    Encontra o menor conjunto de estações de rádio para cobrir todos os estados.
    """
    # 1. Inicialização
    # Conjunto de estados que ainda precisam de cobertura.
    estados_abranger = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    # Dicionário de estações disponíveis e os estados que cada uma cobre.
    estacoes = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }

    # Conjunto final de estações que serão escolhidas.
    estacoes_finais = set()

    # 2. Loop Principal
    # Continua enquanto ainda houver estados para cobrir.
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()

        # Itera sobre cada estação para encontrar a "melhor" opção no momento.
        for estacao, estados_por_estacao in estacoes.items():
            # Calcula a interseção: quais estados necessários esta estação cobre?
            cobertos = estados_abranger & estados_por_estacao

            # Se esta estação cobre mais estados do que a melhor encontrada até agora...
            if len(cobertos) > len(estados_cobertos):
                # ...ela se torna a nova "melhor estação".
                melhor_estacao = estacao
                estados_cobertos = cobertos

        # 3. Atualização
        # Remove os estados recém-cobertos do conjunto de estados a abranger.
        estados_abranger -= estados_cobertos
        # Adiciona a melhor estação encontrada nesta iteração ao conjunto final.
        estacoes_finais.add(melhor_estacao)

    return estacoes_finais


if __name__ == "__main__":
    resultado = aproximacao_gulosa()
    print("As melhores estações para cobrir todos os estados são:")
    # A saída pode variar, mas o resultado é uma solução válida.
    print(resultado)
