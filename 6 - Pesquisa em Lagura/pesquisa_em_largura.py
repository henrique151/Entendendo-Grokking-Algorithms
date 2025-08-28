from collections import deque

# O grafo (a rede de contatos)
grafo = {}
grafo["Você"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    """Verifica se o nome de uma pessoa termina com 'm'."""
    return nome[-1] == 'm'


def pesquisa(nome):
    """Realiza uma pesquisa em largura para encontrar um vendedor de manga."""
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    # Usar um set para 'verificadas' é mais eficiente (O(1) para busca)
    verificadas = set()
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga !")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.add(pessoa)
    return False


if not pesquisa("Você"):
    print("Nenhum vendedor de manga encontrado.")
