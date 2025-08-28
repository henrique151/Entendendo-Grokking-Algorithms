# Capítulo 2: Ordenação por Seleção

Este projeto implementa um dos algoritmos de ordenação mais intuitivos: a **Ordenação por Seleção** (Selection Sort).

## O que é?

A Ordenação por Seleção é um algoritmo simples que divide a lista em duas partes: uma parte ordenada (que começa vazia) e uma parte não ordenada (que começa com a lista inteira). A cada passo, ele encontra o menor elemento da parte não ordenada e o move para o final da parte ordenada.

## Como Funciona? (Passo a Passo)

Imagine que você tem uma lista de números `[64, 25, 12, 22, 11]`. O algoritmo funciona assim:

1.  **Encontre o menor:** Percorra toda a lista e encontre o menor elemento. No nosso caso, é o **11**.
2.  **Mova para a nova lista:** Adicione o **11** a uma nova lista ordenada e remova-o da lista original.
    - _Lista Ordenada:_ `[11]`
    - _Lista Original:_ `[64, 25, 12, 22]`
3.  **Repita:** Encontre o menor elemento na lista restante (**12**), adicione-o à lista ordenada e remova-o da original.
    - _Lista Ordenada:_ `[11, 12]`
    - _Lista Original:_ `[64, 25, 22]`
4.  **Continue** o processo até que a lista original esteja vazia.

Ao final, a nova lista conterá todos os elementos da lista original, mas em ordem crescente.

## Análise de Desempenho (Notação Big O)

A Ordenação por Seleção tem uma complexidade de tempo de **O(n²)** (lê-se "O de n ao quadrado").

- Para encontrar o menor elemento em uma lista de `n` itens, você precisa percorrer todos os `n` itens.
- Você precisa fazer isso `n` vezes (uma vez para cada item da lista).
- Portanto, o número total de operações é aproximadamente `n * n`, ou `n²`.

Isso significa que o tempo de execução cresce de forma quadrática. Se você dobrar o número de itens, o tempo de execução será quadruplicado. Por isso, **não é um algoritmo eficiente para listas grandes**, mas sua simplicidade o torna útil para fins didáticos e para listas pequenas.

## Implementação (`ordenacao_por_selecao.py`)

O script Python contém duas funções principais:

- `busca_menor(arr)`: Encontra e retorna o índice do menor elemento em uma lista.
- `ordenacao_por_selecao(arr)`: Executa o loop principal, chamando `busca_menor` repetidamente para construir a nova lista ordenada.

### Como Executar

Para ver o algoritmo em ação, basta executar o script:

```bash
python ordenacao_selecao.py
```
