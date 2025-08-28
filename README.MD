Livro_Entendendo_Algoritmos

# Meus Estudos sobre Algoritmos

Este repositório é o meu diário de bordo pessoal durante o estudo do livro **"Entendendo Algoritmos" (Grokking Algorithms)**. O objetivo é documentar meu aprendizado, com exemplos de código, exercícios e explicações, para que eu possa revisitar e relembrar esses conceitos fundamentais no futuro.

Cada capítulo do livro é organizado em sua própria pasta, contendo o código-fonte e um `README.md` com detalhes específicos sobre o tema abordado.

## Estrutura dos Capítulos

Aqui está um resumo do que cada capítulo aborda:

### 📂 `1 - Introducao a Algoritmos`

A base de tudo. Apresenta o que é um algoritmo e a importância de medir sua eficiência através da **Notação Big O**. O exemplo central é a **Pesquisa Binária**, um algoritmo de busca extremamente rápido com complexidade **O(log n)**.

### 📂 `2 - Ordenacao Por Seleção`

Explora um dos algoritmos de ordenação mais simples, a **Ordenação por Seleção**. É um ótimo ponto de partida para entender algoritmos de ordenação, apesar de sua baixa eficiência **O(n²)**.

### 📂 `3 - Recursão`

Introduz o conceito poderoso e elegante da **recursão**, onde uma função chama a si mesma. É a base para algoritmos mais complexos, como o Quicksort.

### 📂 `4 - Quicksort`

Apresenta o **Quicksort**, um algoritmo de ordenação muito eficiente que usa a estratégia de **Dividir para Conquistar**. Sua complexidade média é **O(n log n)**, tornando-o um dos mais rápidos na prática.

### 📂 `5 - Tabelas Hash`

Mergulha nas **Tabelas Hash** (dicionários em Python), uma estrutura de dados incrivelmente versátil que mapeia chaves a valores com uma velocidade média de **O(1)**. Essencial para caches, bancos de dados e muito mais.

### 📂 `6 - Pesquisa em Largura`

Aborda a **Pesquisa em Largura (BFS)**, um algoritmo para percorrer grafos. É a ferramenta perfeita para encontrar o caminho mais curto em grafos não ponderados, como em redes sociais.

### 📂 `7 - Algoritmo Dijkstra`

Expande o conceito de busca em grafos com o **Algoritmo de Dijkstra**. Ele encontra o caminho de menor custo em **grafos ponderados**, sendo fundamental para sistemas de GPS e roteamento de redes.

### 📂 `8 - Algoritmos Gulosos`

Explora os **Algoritmos Gulosos**, que resolvem problemas de otimização fazendo a escolha localmente ótima a cada passo. É uma técnica para encontrar uma boa solução aproximada para problemas complexos (NP-difíceis) de forma rápida.

---

## Como Usar

Sinta-se à vontade para navegar pelas pastas. Cada uma é um módulo autocontido com código executável e explicações detalhadas.

```bash
# Exemplo de como executar um script de um capítulo
cd '.\4 - Quicksort\'
python quicksort.py
```
