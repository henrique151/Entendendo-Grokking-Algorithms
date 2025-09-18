# Livro_Entendendo_Algoritmos

# Meus Estudos sobre Algoritmos

Este repositório é o meu diário de bordo pessoal durante o estudo do livro **"Entendendo Algoritmos" (Grokking Algorithms)**. O objetivo é documentar meu aprendizado, com exemplos de código, exercícios e explicações, para que eu possa revisitar e relembrar esses conceitos fundamentais no futuro.

Cada capítulo do livro é organizado em sua própria pasta, contendo o código-fonte e um `README.md` com detalhes específicos sobre o tema abordado.

## Estrutura dos Capítulos

Aqui está um resumo do que cada capítulo aborda:

### 📂 `1 - Introducao a Algoritmos`

**O que é:**  
Apresenta o que é um algoritmo e a importância de medir sua eficiência utilizando a **Notação Big O**.

**Para que serve:**  
Introduz o conceito de algoritmos eficientes e exemplifica com a **Pesquisa Binária**, demonstrando a eficiência de algoritmos com complexidade **O(log n)**.

---

### 📂 `2 - Ordenacao Por Seleção`

**O que é:**  
Explora a **Ordenação por Seleção**, um dos algoritmos de ordenação mais simples.

**Para que serve:**  
Embora não seja o mais eficiente (complexidade **O(n²)**), ele serve para introduzir a ideia de ordenação e comparação entre elementos, preparando o terreno para métodos mais avançados.

---

### 📂 `3 - Recursao`

**O que é:**  
Introduz o conceito fundamental da **recursão**, onde uma função se chama repetidamente.

**Para que serve:**  
A recursão é a base para a solução de problemas complexos, como a abordagem "Dividir para Conquistar", e é utilizada em algoritmos como o Quicksort.

---

### 📂 `4 - Quicksort`

**O que é:**  
Apresenta o **Quicksort**, um algoritmo de ordenação rápido que utiliza a estratégia de **Dividir para Conquistar**.

**Para que serve:**  
Por sua complexidade média de **O(n log n)**, o Quicksort é um dos algoritmos de ordenação mais utilizados na prática, adequado para grandes conjuntos de dados.

---

### 📂 `5 - Tabelas Hash`

**O que é:**  
Aborda a estrutura das **Tabelas Hash**, que mapeiam chaves a valores de forma quase instantânea.

**Para que serve:**  
Essencial para a implementação de caches, bancos de dados e soluções que exigem consultas rápidas, pois possuem eficiência média de **O(1)**.

---

### 📂 `6 - Pesquisa em Largura`

**O que é:**  
Implementa a **Pesquisa em Largura (BFS)**, um algoritmo para percorrer grafos camada a camada.

**Para que serve:**  
Muito útil para encontrar o caminho mais curto em grafos não ponderados, com aplicações em redes sociais, mapeamento e resolução de puzzles.

---

### 📂 `7 - Algoritmo Dijkstra`

**O que é:**  
Expande o universo da busca em grafos com o **Algoritmo de Dijkstra**, que encontra o caminho de menor custo em grafos ponderados.

**Para que serve:**  
Fundamental para sistemas de roteamento, como navegação GPS e redes de comunicação, onde cada aresta tem um peso/custo associado.

---

### 📂 `8 - Algoritmos Gulosos`

**O que é:**  
Explora os **Algoritmos Gulosos**, que fazem escolhas locais ótimas na esperança de alcançar uma solução global satisfatória.

**Para que serve:**  
Utilizados para resolver problemas de otimização rapidamente, como o **Problema da Cobertura de Conjuntos**, onde a solução exata pode ser inviável computacionalmente.

---

### 📂 `9 - Programação Dinâmica`

**O que é:**  
Apresenta a **Programação Dinâmica**, técnica que resolve problemas dividindo-os em subproblemas sobrepostos e armazenando seus resultados para evitar cálculos repetitivos.

**Para que serve:**  
Melhora significativamente a eficiência de algoritmos recursivos, como o cálculo da sequência de Fibonacci e da maior subsequência comum, transformando abordagens exponenciais em soluções polinomiais.

---

### 📂 `10 - K-Vizinhos Mais Próximos (KNN)`

**O que é:**  
Implementa o algoritmo dos **K-Vizinhos Mais Próximos (KNN)**, utilizado para classificação e regressão.

**Para que serve:**  
Classifica novos pontos com base na proximidade com pontos previamente classificados, servindo em aplicações como reconhecimento de padrões, diagnósticos médicos e sistemas de recomendação.

---

### 📂 `11 - Próximos Passos`

**O que é:**  
Apresenta exemplos simples de tópicos avançados, incluindo:

- **Árvores:** Estruturas hierárquicas e seus percursos.
- **Índices Invertidos:** Técnica essencial para motores de busca.
- **Algoritmos Paralelos:** Utilização de multiprocessamento para acelerar cálculos.
- **Filtro de Bloom e HyperLogLog:** Algoritmos probabilísticos para verificação de pertencimento e estimativa de cardinalidade.

**Para que serve:**  
Estes exemplos demonstram técnicas avançadas e práticas que podem ser aplicadas em sistemas de grande escala, otimização de performance e segurança da informação.

---

## Como Usar

Sinta-se à vontade para navegar pelas pastas. Cada capítulo contém código executável e explicações detalhadas que podem ser consultadas conforme o seu interesse.

```bash
# Exemplo de como executar um script de um capítulo
cd '.\4 - Quicksort\'
python quicksort.py
```

Explore, aprenda e adapte os exemplos de acordo com as necessidades de seus projetos e estudos.

---
