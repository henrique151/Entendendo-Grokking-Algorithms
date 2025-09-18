# K-Vizinhos Mais Próximos (KNN)

Este projeto implementa o algoritmo **K-Vizinhos Mais Próximos** (k-nearest neighbors - KNN), uma técnica simples e eficaz utilizada em problemas de classificação e regressão.

## O que é?

O algoritmo KNN classifica um novo ponto de dados com base na proximidade dos seus vizinhos mais próximos em um conjunto de dados pré-classificados. Para isso, é utilizado um método de medida de distância, como a distância Euclidiana, para identificar quais são os pontos mais próximos do novo dado.

## Para que serve?

- **Classificação:** Identificar a categoria ou rótulo de um novo dado, baseado na maioria dos rótulos dos seus vizinhos mais próximos.
- **Regressão:** Prever um valor contínuo (embora este exemplo foque na classificação).
- **Aplicações:** Diagnóstico médico, reconhecimento de padrões, sistemas de recomendação, entre outros.

## Como funciona?

1. **Cálculo da Distância:** Para cada ponto de treinamento, calcula-se a distância até o ponto a ser classificado.
2. **Seleção dos Vizinhos:** Ordena-se os pontos pela distância e seleciona-se os K vizinhos mais próximos.
3. **Votação:** Realiza-se uma votação simples entre os rótulos dos vizinhos e o rótulo majoritário é atribuído ao novo ponto.

## Exemplo de Execução

Para ver o algoritmo em ação, basta executar:

```bash
python k_vizinhos_mais_proximos.py
```

A saída exibirá a classificação de um exemplo de ponto testado.
