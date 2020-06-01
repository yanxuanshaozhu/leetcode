# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

# Input: m = 3, n = 2
# Output: 3


def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for j in range(m)] for i in range(n)]
    for j in range(m):
        dp[0][j] = 1
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    print(uniquePaths(3, 2))
