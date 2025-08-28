# Neste exemplo simples:
# - Uma "caixa" é representada por uma lista.
# - Um "item" dentro da caixa pode ser uma string ou outra lista (uma sub-caixa).
def procurar_chave(caixa):
    """
    Procura recursivamente pela string 'chave' em uma estrutura de listas aninhadas.
    """
    print(f"Olhando dentro da caixa com os itens: {caixa}")
    for item in caixa:
        if isinstance(item, list):
            # Caso Recursivo: Se o item é outra caixa (lista), chama a função para ela.
            if procurar_chave(item):
                return True  # Propaga o sinal de "encontrado" para cima.
        elif item == 'chave':
            # Caso Base: Se o item é a chave, encontramos!
            print("Achei a chave!")
            return True
    return False  # Retorna False se a chave não foi encontrada nesta caixa.


if __name__ == "__main__":
    # Nossa estrutura de caixas aninhadas, agora usando listas e strings.
    # A chave está dentro de duas caixas.
    caixa_principal = ['livro', 'celular', [
        'parafuso', 'prego', ['adesivo', 'chave']]]

    print("Iniciando a busca pela chave na caixa principal...")
    print("-" * 20)
    if not procurar_chave(caixa_principal):
        print("A chave não foi encontrada em nenhuma caixa.")
