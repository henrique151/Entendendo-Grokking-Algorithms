def fibonacci(n, memo={}):
    """
    Calcula o n-ésimo número de Fibonacci utilizando memoization para otimização.

    Parâmetros:
    - n: índice do número de Fibonacci desejado.
    - memo: dicionário para armazenar os resultados já calculados.

    Retorna:
    - O n-ésimo número de Fibonacci.
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


if __name__ == "__main__":
    n = 10  # Exemplo: calcular o 10º número de Fibonacci
    print(f"O {n}º número de Fibonacci é: {fibonacci(n)}")
