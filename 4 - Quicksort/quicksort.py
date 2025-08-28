from typing import List


def quicksort(array: List[int]) -> List[int]:
    """
    Ordena uma lista usando o algoritmo Quicksort com uma abordagem recursiva.
    """
    # Caso base: listas com 0 ou 1 elemento já estão "ordenadas".
    if len(array) < 2:
        return array
    else:
        # Caso recursivo
        pivo = array[0]
        # Sub-lista de todos os elementos menores que o pivô
        menores = [i for i in array[1:] if i <= pivo]
        # Sub-lista de todos os elementos maiores que o pivô
        maiores = [i for i in array[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)


if __name__ == "__main__":
    minha_lista = [10, 5, 2, 3, 99, 45, 1, 0]
    print(f"Lista original: {minha_lista}")
    print(f"Lista ordenada: {quicksort(minha_lista)}")
