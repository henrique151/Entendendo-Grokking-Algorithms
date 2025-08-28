# Capítulo 3: Recursão

Este projeto demonstra o conceito de **recursão** usando um exemplo clássico: procurar por uma chave dentro de uma pilha de caixas aninhadas.

## O que é Recursão?

Recursão é uma técnica de programação onde uma função chama a si mesma para resolver um problema. Uma função recursiva divide o problema em subproblemas menores e mais simples, até que atinja um **caso base**, que é um problema tão simples que pode ser resolvido diretamente, sem mais chamadas recursivas.

Toda função recursiva precisa de duas partes:

1.  **Caso Base:** A condição que para a recursão. Sem ele, a função entraria em um loop infinito.
2.  **Caso Recursivo:** A parte da função que se chama novamente, mas com uma entrada que a aproxima do caso base.

## Para que serve?

A recursão é uma maneira elegante de resolver problemas que podem ser divididos em problemas semelhantes de menor escala. É muito comum em:

- **Estruturas de Dados em Árvore ou Grafo:** Navegar em sistemas de arquivos, árvores de decisão, etc.
- **Algoritmos de Divisão e Conquista:** Como Quicksort e Mergesort.
- **Problemas Matemáticos:** Como o cálculo de fatoriais ou a sequência de Fibonacci.

## O Exemplo: Procurando pela Chave

No script `recursao_procurar_chave.py`, simulamos a tarefa de encontrar uma chave escondida em uma de várias caixas, que podem conter outras caixas.

### Como a Implementação Funciona

1.  **Estrutura de Dados:**

    - Criamos duas classes simples: `Caixa` e `Chave`.
    - Uma `Caixa` pode conter uma lista de `itens`, que podem ser outras `Caixas` ou uma `Chave`.

2.  **A Função Recursiva `procurar_chave(caixa)`:**
    - **Caso Recursivo:** A função itera sobre os itens dentro de uma `caixa`. Se um `item` é outra `Caixa`, a função chama a si mesma (`procurar_chave(item)`) para procurar dentro dessa nova caixa.
    - **Caso Base:** Se um `item` é uma `Chave`, a função imprime "Achei a chave!" e a recursão para.

### Como Executar

Para ver o algoritmo em ação, basta executar o script Python:

```bash
python recursao_procurar_chave.py
```

A saída mostrará o passo a passo de como o algoritmo "abre" cada caixa até encontrar a chave.
