def minDistance(word1: str, word2: str) -> tuple:
    nrow = len(word1) + 1
    ncol = len(word2) + 1
    dp = [[0] * ncol for _ in range(nrow)]
    for _ in range(ncol):
        dp[0][_] = _
    for _ in range(nrow):
        dp[_][0] = _
    for i in range(1, nrow):
        for j in range(1, ncol):
            dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1,
                           dp[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0))

    return dp[-1][-1]


if __name__ == "__main__":
    print(minDistance("horse", "ros"))
