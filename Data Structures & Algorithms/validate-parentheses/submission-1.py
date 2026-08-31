class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in ')}]':
                if not stack: return False
                if stack.pop() != mapping[ch]: return False
            else:
                stack.append(ch)
        return not stack