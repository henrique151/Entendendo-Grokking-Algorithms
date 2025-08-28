# Algoritmo de Dijkstra

Este projeto contém uma implementação em Python do Algoritmo de Dijkstra, baseada nos conceitos do livro "Entendendo Algoritmos" (Grokking Algorithms).

## O que é?

O Algoritmo de Dijkstra é um dos algoritmos mais famosos para encontrar o **caminho mais curto (ou de menor custo)** entre um nó inicial e todos os outros nós em um grafo ponderado. Um grafo ponderado é aquele em que cada aresta (conexão) tem um "peso" ou "custo" associado.

A principal característica do algoritmo é que ele funciona para grafos com **pesos não negativos** (ou seja, os custos não podem ser menores que zero).

## Para que serve?

O Algoritmo de Dijkstra é fundamental em diversas aplicações do mundo real, como:

- **Sistemas de GPS e Mapas:** Calcular a rota mais rápida ou mais curta entre dois pontos.
- **Roteamento de Redes:** Encontrar o caminho mais eficiente para pacotes de dados viajarem de um roteador para outro na internet.
- **Logística e Transporte:** Determinar a rota mais barata para uma entrega.
- **Planejamento de Voos:** Encontrar a combinação de voos com o menor custo ou tempo de viagem.

## Como o algoritmo funciona?

O algoritmo funciona de forma iterativa, sempre mantendo uma estimativa do caminho mais curto do ponto de partida até cada nó.

1.  **Inicialização:**

    - Crie uma tabela de `custos` para armazenar o custo para chegar a cada nó a partir do início. Inicialize o custo do nó inicial como 0 (ou o custo de seus vizinhos diretos) e todos os outros como infinito (`∞`).
    - Crie uma tabela de `pais` para reconstruir o caminho. Ela armazena de qual nó viemos para chegar ao nó atual pelo caminho mais barato.
    - Crie uma lista de `processados` para não verificar o mesmo nó duas vezes.

2.  **Iteração:**

    - Enquanto houver nós não processados, encontre o nó "mais barato" (com o menor custo na tabela `custos`) que ainda não foi processado.

3.  **Atualização dos Vizinhos:**

    - Para o nó atual, verifique todos os seus vizinhos.
    - Para cada vizinho, calcule o custo para chegar até ele _passando pelo nó atual_.
    - Se esse novo custo for menor do que o custo já registrado na tabela `custos`, atualize a tabela com o novo custo e atualize a tabela `pais` para registrar que o caminho mais barato para este vizinho agora passa pelo nó atual.

4.  **Conclusão:**
    - Marque o nó atual como processado.
    - Repita o processo a partir do passo 2.

O algoritmo termina quando todos os nós alcançáveis foram processados. Ao final, a tabela `custos` conterá o menor custo do nó inicial para todos os outros nós.

## Implementação neste Projeto (`algoritmo_de_dijkstra.py`)

O script `algoritmo_de_dijkstra.py` implementa essa lógica usando estruturas de dados simples do Python.

### Estruturas de Dados

- **`grafo` (dicionário):** Representa o mapa. As chaves são os nós, e os valores são outros dicionários contendo os vizinhos e os custos (pesos) para alcançá-los.
- **`custos` (dicionário):** Armazena o menor custo conhecido do `"inicio"` até cada nó.
- **`pais` (dicionário):** Armazena o nó pai no caminho mais curto. Essencial para reconstruir a rota no final.
- **`processados` (lista):** Guarda os nós que já foram analisados para não entrarmos em loops.

### Funções

- **`ache_no_custo_mais_baixo(custos)`:** Uma função auxiliar que varre a tabela de custos e retorna a chave do nó mais barato que ainda não foi processado.
- **`dijkstra()`:** A função principal que executa o loop do algoritmo até que todos os nós sejam processados.

### Como Executar

Para ver o algoritmo em ação, basta executar o script Python no seu terminal:

```bash
python algoritmo_dijkstra.py
```

A saída mostrará os custos finais do nó "inicio" para todos os outros nós do grafo, incluindo o custo total para chegar ao "fim".

```
Custo do início para cada nó:
{'a': 5, 'b': 2, 'fim': 6}
Caminho mais barato encontrado tem o custo de: 6
```
