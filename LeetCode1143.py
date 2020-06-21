def longestCommonSubsequence(text1: str, text2: str) -> int:
    nrow = len(text1) + 1
    ncol = len(text2) + 1
    ls = [[0] * ncol for x in range(nrow)]  # list comprehension is faster using np.ndarray
    for i in range(1, nrow):
        for j in range(1, ncol):
            if text1[i - 1] == text2[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
            else:
                if ls[i - 1][j] >= ls[i][j - 1]:
                    ls[i][j] = ls[i - 1][j]
                else:
                    ls[i][j] = ls[i][j - 1]
    return ls[-1][-1]


if __name__ == "__main__":
    print(longestCommonSubsequence("123", "234"))
