# 泰波那契序列 Tn 定义如下： 
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

"""
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)              this has complexity of O(N^3)

"""


def tribonacci1(n: int) -> int:
    if n < 3:
        return 1 if n else 0  # Speed up ,for n < 3, we dont need to use loop to calculate the result
    x, y, z = 0, 1, 1
    for i in range(n):
        x, y, z = y, z, x + y + z
    return x


#  Time complexity O(N): n loop; Space complexity: O(1): only saves three numbers


class Tri:
    def __init__(self):
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]


def tribonacci2(n: int) -> int:
    return Tri().nums[n]


if __name__ == "__main__":
    print(tribonacci1(10))
    print(tribonacci2(10))
