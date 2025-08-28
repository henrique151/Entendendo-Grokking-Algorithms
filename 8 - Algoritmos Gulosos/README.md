# Algoritmos Gulosos

Este projeto implementa um algoritmo guloso para resolver o **Problema da Cobertura de Conjuntos** (Set Covering Problem). O exemplo específico é encontrar o menor número de estações de rádio para cobrir uma lista de estados nos EUA.

## O que é?

Um algoritmo guloso é uma abordagem para resolver problemas de otimização que faz a escolha **localmente ótima** em cada etapa, na esperança de encontrar uma solução **globalmente ótima** (ou pelo menos uma boa aproximação).

Em vez de analisar todas as possibilidades, ele simplesmente escolhe a melhor opção disponível no momento e segue em frente.

## Para que serve?

Algoritmos gulosos são extremamente úteis para encontrar soluções rápidas e eficientes para problemas complexos onde a solução perfeita é computacionalmente inviável. Algumas aplicações práticas incluem:

- **Problema da Cobertura de Conjuntos:** Como no exemplo, selecionar locais para antenas de celular, hospitais ou centros de distribuição para cobrir uma região com o menor custo.
- **Agendamento e Alocação de Recursos:** Escalonar tarefas em processadores ou agendar aulas em salas de aula para maximizar o uso dos recursos.
- **Algoritmo de Huffman:** Usado em compressão de dados (como em arquivos `.zip`) para criar códigos de tamanho variável e eficientes para caracteres.
- **Problema do Troco:** Dar o troco usando o menor número possível de moedas (em alguns sistemas monetários).
- **Algoritmos de Caminho Mínimo:** Variações como o algoritmo de Dijkstra e o de Prim (para árvores geradoras mínimas) usam uma abordagem gulosa.

## O Problema da Cobertura de Conjuntos

Imagine que você tem um conjunto de elementos (no nosso caso, estados) que precisam ser "cobertos". Você também tem uma coleção de conjuntos (estações de rádio), onde cada um cobre alguns desses elementos.

O objetivo é selecionar o **menor número de conjuntos (estações) possível** para que todos os elementos (estados) sejam cobertos.

Este é um problema **NP-difícil**, o que significa que encontrar a solução perfeita pode levar um tempo extremamente longo para um grande número de estações. É por isso que usamos um algoritmo de aproximação, como o guloso.

## Como a Implementação Funciona

O script `algoritmo_guloso.py` resolve o problema da seguinte forma:

1.  **Inicialização:**

    - `estados_abranger`: Um conjunto com todos os estados que precisam de cobertura.
    - `estacoes`: Um dicionário onde cada chave é uma estação e o valor é o conjunto de estados que ela cobre.
    - `estacoes_finais`: Um conjunto vazio que armazenará nossa solução.

2.  **Loop Guloso:**

    - O algoritmo entra em um loop que continua enquanto houver estados em `estados_abranger`.
    - Em cada iteração, ele procura a **"melhor" estação**: aquela que cobre o maior número de estados _que ainda não foram cobertos_.

3.  **Seleção e Atualização:**

    - Uma vez que a melhor estação é encontrada, ela é adicionada a `estacoes_finais`.
    - Os estados que essa estação cobre são removidos de `estados_abranger`.

4.  **Conclusão:**
    - O loop se repete até que `estados_abranger` esteja vazio.
    - Ao final, `estacoes_finais` contém um subconjunto de estações que, juntas, cobrem todos os estados. Embora não seja garantido que seja a solução _perfeita_, é uma aproximação muito boa e rápida de se obter.

### Como Executar

```bash
python algoritmo_guloso.py
```
