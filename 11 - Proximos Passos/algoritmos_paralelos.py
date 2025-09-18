import multiprocessing


def somar_parcial(dados):
    return sum(dados)


if __name__ == "__main__":
    dados = list(range(1, 101))  # Soma de 1 a 100
    n_processos = 4
    tamanho = len(dados) // n_processos
    partes = [dados[i * tamanho:(i + 1) * tamanho] for i in range(n_processos)]

    with multiprocessing.Pool(processes=n_processos) as pool:
        resultados = pool.map(somar_parcial, partes)

    soma_total = sum(resultados)
    print(f"Soma total: {soma_total}")
