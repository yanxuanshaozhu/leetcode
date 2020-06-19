# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Input: num1 = "123", num2 = "456"
# Output: "56088"


def multiply(str1, str2):
    result = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            result += int(str1[i]) * 10 ** (len(str1) - 1 - i) * int(str2[j]) * 10 ** (len(str2) - 1 - j)
    return str(result)


if __name__ == "__main__":
    print(multiply("12345678910", "456789999"))
    print(12345678910 * 456789999)
