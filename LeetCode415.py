def addString(num1: str, num2: str) -> str:
    longer = num1 if len(num1) >= len(num2) else num2
    shorter = num2 if len(num1) >= len(num2) else num1
    ls = [0] * (len(longer) + 1)
    for i in range(len(shorter)):
        ls[i] += int(shorter[len(shorter) - 1 - i])
    for i in range(len(longer)):
        ls[i] += int(longer[len(longer) - 1 - i])
    for i in range(len(ls) - 1):
        if ls[i] >= 10:
            temp = ls[i]
            ls[i] = temp % 10
            ls[i + 1] += temp // 10
    high = ls[-1]
    while high == 0 and len(ls) > 1:
        ls.pop()
        high = ls[-1]
    ls.reverse()
    return "".join([str(x) for x in ls])


if __name__ == "__main__":
    print(addString("0", "0"))
