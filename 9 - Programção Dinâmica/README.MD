# Programação Dinâmica

Este projeto explora a **Programação Dinâmica**, uma técnica poderosa para resolver problemas que podem ser divididos em subproblemas sobrepostos. Em muitos casos, métodos recursivos simples repetem os mesmos cálculos diversas vezes. A Programação Dinâmica melhora a eficiência armazenando os resultados intermediários para não recalcular os mesmos valores mais de uma vez.

## O que é Programação Dinâmica?

A Programação Dinâmica é usada quando um problema pode ser dividido em subproblemas menores que se sobrepõem. A ideia é resolver cada subproblema uma única vez e armazenar sua solução — geralmente usando **memoization** (armazenamento em cache) ou **tabulação** (solução bottom-up).

## Para que serve?

A Programação Dinâmica é utilizada para resolver problemas que podem ser divididos em subproblemas repetitivos. Ao armazenar os resultados intermediários, evita-se a recomputação dos mesmos valores, o que torna algoritmos recursivos, como o cálculo da sequência de Fibonacci, muito mais eficientes.

## Como funciona?

A técnica se baseia na identificação dos subproblemas sobrepostos e na utilização de uma estratégia de armazenamento (como _memoization_ ou tabulação) para guardar os resultados parciais. Assim:

- **Memoization:** Utiliza recursão com um cache que armazena os resultados já calculados.
- **Tabulação:** Resolve os subproblemas de forma iterativa, construindo uma tabela de resultados.

## Exemplo de Aplicação

Um exemplo clássico, e mencionado no _Grokking Algorithms_, é o cálculo da sequência de Fibonacci. Na abordagem recursiva simples, muitos cálculos idênticos são realizados repetidamente. Com a Programação Dinâmica, usamos um cache para armazenar os resultados intermediários, melhorando consideravelmente o desempenho.

## Como Executar

Para ver o exemplo em ação, execute o script:

```bash
python dynamic_programming.py
```

```bash
python dynamic_programming2.py
```

A saída exibirá os números Fibonacci calculados de forma eficiente com a técnica de memoization.
