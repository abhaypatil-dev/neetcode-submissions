class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                # pop two numbers - a, b
                b = int(stack.pop())
                a = int(stack.pop())

                # apply operation
                result = self.applyOperation(a, b, token)

                # append result
                stack.append(result)
            else:
                stack.append(token)
            # print(stack)

        return int(stack.pop())

    def applyOperation(self, a, b, op):
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/": return int(a / b)
        
# 10 6 9 3
# 10 6 -132