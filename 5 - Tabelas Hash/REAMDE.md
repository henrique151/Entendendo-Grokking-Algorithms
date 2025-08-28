# Tabelas Hash

Este capítulo explora as **Tabelas Hash** (também conhecidas como dicionários, mapas ou arrays associativos), uma das estruturas de dados mais úteis e versáteis da computação.

## O que são?

Uma Tabela Hash é uma estrutura de dados que mapeia **chaves** a **valores**. Ela faz isso usando uma **função de hash**, que converte uma chave (por exemplo, uma string) em um índice numérico de um array. Esse índice é usado para armazenar ou recuperar o valor associado à chave.

A grande vantagem é que, em média, essa operação de busca, inserção e remoção é extremamente rápida.

## Para que servem?

Tabelas Hash são usadas em todos os lugares:

- **Dicionários em Python:** A implementação interna do `dict` do Python é uma tabela hash.
- **Bancos de Dados:** Para indexar e recuperar dados rapidamente.
- **Cache:** Para armazenar resultados de operações caras e recuperá-los rapidamente (ex: um site que armazena uma página da web para não ter que gerá-la novamente).
- **Prevenção de Duplicatas:** Verificar se um item já existe em uma coleção.
- **Listas Telefônicas:** Associar nomes a números de telefone.

## Análise de Desempenho (Notação Big O)

- **Caso Médio:** A inserção, busca e remoção em uma tabela hash levam tempo **O(1)**, ou seja, tempo constante. Não importa se a tabela tem 10 ou 10 milhões de itens, a operação leva praticamente o mesmo tempo.
- **Pior Caso:** Quando ocorrem muitas **colisões** (diferentes chaves geram o mesmo índice), o desempenho pode degradar para **O(n)**. Boas funções de hash minimizam a chance de isso acontecer.

## Implementação (`tabela_hash.py`)

O Python já nos fornece uma implementação de tabela hash robusta e otimizada: o **dicionário (`dict`)**.

O script `tabela_hash.py` demonstra dois casos de uso comuns:

1.  **Lista de Preços:** Mapeando o nome de um item ao seu preço.
2.  **Cache de Votos:** Verificando se uma pessoa já votou para evitar votos duplicados.

### Como Executar

Para ver os exemplos em ação, execute o script:

```bash
python tabela_hash.py
```
