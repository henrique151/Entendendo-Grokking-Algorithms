import math
from collections import Counter


def euclidean_distance(point1, point2):
    """
    Calcula a distância Euclidiana entre dois pontos.

    Parâmetros:
      - point1, point2: sequências numéricas que representam as coordenadas dos pontos.

    Retorna:
      - Distância Euclidiana entre point1 e point2.
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def knn_classificar(treinamento, ponto_teste, k):
    """
    Classifica um ponto utilizando o algoritmo dos K-vizinhos mais próximos.

    Parâmetros:
      - treinamento: lista de tuplas no formato (características, rótulo)
      - ponto_teste: lista de características do ponto a ser classificado.
      - k: número de vizinhos a serem considerados.

    Retorna:
      - O rótulo classificado para o ponto_teste.
    """
    distancias = []

    # Calcula a distância entre o ponto_teste e cada ponto do conjunto de treinamento
    for features, rotulo in treinamento:
        distancia = euclidean_distance(features, ponto_teste)
        distancias.append((distancia, rotulo))

    # Ordena as distâncias e seleciona os k vizinhos mais próximos
    distancias.sort(key=lambda x: x[0])
    k_vizinhos = [rotulo for _, rotulo in distancias[:k]]

    # Realiza a votação e retorna o rótulo com a maioria dos votos
    votos = Counter(k_vizinhos)
    return votos.most_common(1)[0][0]


if __name__ == "__main__":
    # Exemplo de dados de treinamento: (características, rótulo)
    treinamento = [
        ([2.0, 3.0], 'A'),
        ([1.0, 1.0], 'A'),
        ([4.0, 5.0], 'B'),
        ([5.0, 5.0], 'B'),
        ([1.5, 1.8], 'A'),
        ([3.5, 4.5], 'B')
    ]

    # Ponto que queremos classificar
    ponto_teste = [3.0, 3.5]
    k = 3

    rotulo_classificado = knn_classificar(treinamento, ponto_teste, k)
    print(
        f"O ponto {ponto_teste} foi classificado como: {rotulo_classificado}")
