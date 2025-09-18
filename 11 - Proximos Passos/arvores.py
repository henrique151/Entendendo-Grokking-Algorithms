class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def inorder(node):
    if node:
        inorder(node.esquerda)
        print(node.valor, end=" ")
        inorder(node.direita)


if __name__ == "__main__":
    # Criação de uma árvore binária simples
    raiz = Node(10)
    raiz.esquerda = Node(5)
    raiz.direita = Node(15)
    raiz.esquerda.esquerda = Node(3)
    raiz.esquerda.direita = Node(7)

    print("Percurso in-order da árvore:")
    inorder(raiz)
    print()
