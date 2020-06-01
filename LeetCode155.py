# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。

import math


class MinStack:

    def __init__(self):
        self.items = []
        self.backup = [math.inf] 

    def push(self, x: int) -> None:
        self.items.append(x)
        self.backup.append(min(x, self.backup[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.backup.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.backup[-1]

    def display(self):
        for ele in self.items:
            print(ele)


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
