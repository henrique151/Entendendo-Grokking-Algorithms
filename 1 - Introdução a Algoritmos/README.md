# Introdução aos Algoritmos

Bem-vindo ao estudo dos algoritmos! Este capítulo serve como a porta de entrada para entender como resolvemos problemas de forma eficiente usando a computação.

## O que é um Algoritmo?

Um algoritmo é simplesmente um **conjunto de instruções passo a passo** para realizar uma tarefa ou resolver um problema. Pense nele como uma receita de bolo: você segue uma sequência de passos para chegar a um resultado final.

No mundo da programação, um algoritmo é a lógica que seu código executa para transformar uma entrada (input) em uma saída (output) desejada.

## Por que a Eficiência é Importante?

Para um mesmo problema, podem existir vários algoritmos diferentes. A grande questão é: qual deles é o melhor?

A "melhor" solução geralmente é a mais **rápida** (leva menos tempo) e a que usa menos **memória**. A eficiência de um algoritmo se torna crucial à medida que a quantidade de dados aumenta. Um algoritmo lento pode levar segundos para processar 100 itens, mas pode levar dias (ou anos!) para processar 1 bilhão de itens.

### Medindo a Eficiência: Notação Big O

A **Notação Big O** é a forma como medimos a eficiência de um algoritmo. Ela não nos diz o tempo exato de execução em segundos, mas descreve como o tempo de execução **cresce** à medida que o tamanho da entrada aumenta.

Por exemplo:

- **Pesquisa Simples (O(n)):** Em uma lista de `n` itens, no pior caso, você precisa olhar todos os `n` itens. Se a lista dobrar de tamanho, o tempo de execução também dobra.
- **Pesquisa Binária (O(log n)):** Em uma lista ordenada de `n` itens, você pode eliminar metade dos itens a cada passo. Se a lista dobrar de tamanho, o tempo de execução aumenta em apenas um passo. É extremamente eficiente!

Entender a Notação Big O é fundamental para escolher o algoritmo certo para o seu problema e escrever um código de alta performance.
