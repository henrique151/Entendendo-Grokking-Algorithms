# Quicksort

Este projeto implementa o **Quicksort**, um algoritmo de ordenação elegante e eficiente que utiliza a estratégia de **Dividir para Conquistar**.

## O que é Dividir para Conquistar?

Dividir para Conquistar (D&C) é uma poderosa abordagem para resolver problemas, que consiste em três passos:

1.  **Dividir:** Quebre o problema grande em subproblemas menores e mais simples.
2.  **Conquistar:** Resolva os subproblemas de forma recursiva. Se eles forem pequenos o suficiente, resolva-os diretamente (este é o **caso base**).
3.  **Combinar:** Junte as soluções dos subproblemas para formar a solução do problema original.

## Como o Quicksort Funciona?

O Quicksort aplica a estratégia D&C para ordenar uma lista:

1.  **Caso Base:** Se a lista tem 0 ou 1 elemento, ela já está ordenada.
2.  **Dividir (Particionar):** Escolha um elemento da lista como **pivô**.
3.  **Conquistar:** Reorganize a lista em duas sub-listas: uma com todos os elementos menores que o pivô e outra com todos os elementos maiores que o pivô.
4.  **Combinar:** Chame o Quicksort recursivamente para as duas sub-listas. A lista final ordenada será a sub-lista dos menores (já ordenada) + o pivô + a sub-lista dos maiores (já ordenada).

## Análise de Desempenho (Notação Big O)

- **Caso Médio:** A complexidade de tempo do Quicksort é **O(n log n)**, o que o torna um dos algoritmos de ordenação mais rápidos na prática.
- **Pior Caso:** Se o pivô escolhido for sempre o menor ou o maior elemento, o desempenho degrada para **O(n²)**, semelhante à Ordenação por Seleção. A escolha de um pivô aleatório ajuda a evitar esse cenário.

## Implementação (`quicksort.py`)

O script implementa o Quicksort de forma recursiva. A função `quicksort` escolhe o primeiro elemento como pivô e cria as sub-listas de "menores" e "maiores" para então chamá-las recursivamente.

### Como Executar

Para ver o algoritmo em ação, execute o script:

```bash
python quicksort.py
```
