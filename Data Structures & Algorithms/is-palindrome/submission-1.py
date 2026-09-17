class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        L, R = 0, n - 1
        while L <= R:
            while L < n and not s[L].isalnum():
                L += 1
            while R >= 0 and not s[R].isalnum():
                R -= 1
            if L > R: return True
            # print(s[L], s[R])
            if s[L].lower() != s[R].lower(): return False
            L += 1
            R -= 1
        return True