# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Input: 121
# Output: true
# Input: -121
# Output: false
# Input: 10
# Output: false


def isPalindrome1(x: int) -> bool:
    result = True
    ls = []
    for ele in str(x):
        ls.append(ele)
    while len(ls) > 1 and result:
        right = ls.pop()
        left = ls.pop(0)
        if right != left:
            result = False
    return result


# Standard Solution:Reverse the last half of the integer
def isPalindrome2(x: int) -> bool:
    result = True
    if x < 0 or (x % 10 == 0 and x != 0):
        result = False
    else:
        rev = 0
        while x > rev:  # When x <= rev, rev > last half of original x
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
        if x == rev or rev // 10 == x:  # When x&1 == True, rev//10 == x
            pass
        else:
            result = False
    return result


if __name__ == "__main__":
    print(isPalindrome1(121))
    print(isPalindrome2(121))
