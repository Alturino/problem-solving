import sys


class MinStack:
    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        minv = min(val, self.minst[-1] if self.minst else val)
        self.minst.append(minv)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        else:
            return -1

    def getMin(self) -> int:
        if self.minst:
            return self.minst[-1]
        return sys.maxsize


# Your MinStack object will be instantiated and called as such:
minst = MinStack()
# minst.push(-2)
# minst.push(0)
# minst.push(-3)
# print(minst.getMin())
# minst.pop()
# print(minst.top())
# print(minst.getMin())

minst.push(-2)
minst.push(0)
minst.push(-1)
print(minst.getMin())
print(minst.top())
minst.pop()
print(minst.getMin())
