# Pesquisa em Largura (BFS)

Este projeto implementa a **Pesquisa em Largura** (Breadth-First Search - BFS), um algoritmo fundamental para percorrer ou pesquisar em estruturas de dados de grafos e árvores.

## O que é?

A Pesquisa em Largura é um algoritmo que explora os vizinhos de um nó "em camadas". Ele começa em um nó raiz e explora todos os seus vizinhos diretos (primeira camada). Em seguida, para cada um desses vizinhos, ele explora seus vizinhos ainda não visitados (segunda camada), e assim por diante.

Para manter a ordem de exploração, o BFS usa uma estrutura de dados de **fila** (First-In, First-Out).

## Para que serve?

O BFS é ideal para encontrar o **caminho mais curto** em um grafo **não ponderado** (onde todas as arestas têm o mesmo "custo"). Suas aplicações incluem:

- **Redes Sociais:** Encontrar o caminho mais curto entre duas pessoas (graus de separação).
- **Roteamento:** Encontrar o menor número de saltos entre dois nós em uma rede.
- **Web Crawlers:** Descobrir todas as páginas de um site a partir da página inicial.
- **Inteligência Artificial:** Encontrar uma solução em um espaço de estados (como em jogos de tabuleiro).

## Como Funciona?

1.  **Inicialização:** Crie uma fila e adicione o nó inicial a ela. Crie também um conjunto para rastrear os nós já visitados.
2.  **Loop:** Enquanto a fila não estiver vazia:
    - Retire o primeiro nó da fila.
    - Verifique se este é o nó que você está procurando. Se for, a busca terminou.
    - Caso contrário, adicione todos os vizinhos deste nó (que ainda não foram visitados) ao final da fila e marque-os como visitados.
3.  **Conclusão:** Se a fila ficar vazia e o nó não for encontrado, significa que não há um caminho até ele.

## Análise de Desempenho (Notação Big O)

A complexidade de tempo do BFS é **O(V + E)**, onde `V` é o número de vértices (nós) e `E` é o número de arestas (conexões). Isso porque, no pior caso, o algoritmo visita cada nó e cada aresta uma única vez.

## Implementação (`pesquisa_em_largura.py`)

O script implementa o BFS para resolver um problema divertido: encontrar um "vendedor de manga" em uma rede social. O algoritmo começa em "Você" e explora sua rede de amigos, camada por camada, até encontrar alguém cujo nome termine com 'm'.

### Como Executar

```bash
python pesquisa_em_largura.py
```
