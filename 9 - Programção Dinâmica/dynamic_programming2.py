def longest_common_subsequence(palavra_a, palavra_b):
    """
    Calcula o comprimento da maior subsequência comum entre palavra_a e palavra_b.

    Parâmetros:
      - palavra_a: string.
      - palavra_b: string.

    Retorna:
      - Comprimento da maior subsequência comum.
    """
    m = len(palavra_a)
    n = len(palavra_b)

    # Inicializa a tabela DP com dimensões (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenche a tabela usando programação dinâmica
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palavra_a[i - 1] == palavra_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    palavra_a = "AGGTAB"
    palavra_b = "GXTXAYB"
    resultado = longest_common_subsequence(palavra_a, palavra_b)
    print(f"Comprimento da maior subsequência comum: {resultado}")
