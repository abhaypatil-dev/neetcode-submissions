class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = 2**31

    def push(self, val: int) -> None:
        self.smallest = min(self.smallest, val)
        self.stack.append((val, self.smallest))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.smallest = self.stack[-1][1]
        else:
            self.smallest = 2**31

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
