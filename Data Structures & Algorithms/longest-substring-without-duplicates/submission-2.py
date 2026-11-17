class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_at = {}
        L = -1
        ans = 0

        for R in range(len(s)):
            if s[R] in seen_at:
                L = max(L, seen_at[s[R]])
            ans = max(ans, R - L)
            seen_at[s[R]] = R

        return ans