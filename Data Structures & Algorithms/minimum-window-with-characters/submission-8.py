class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for ch in t:
            freq_t[ch] += 1

        L = 0
        best_start = 0
        best_len = float("inf")

        for i in range(len(s)):
            freq_s[s[i]] += 1

            while L <= i and self.isValid(freq_s, freq_t):
                window_len = i - L + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = L
                
                freq_s[s[L]] -= 1
                L += 1

        if best_len == float("inf"):
            return ""
        return s[best_start:best_start + best_len]

    def isValid(self, freq_s, freq_t):
        for k, v in freq_t.items():
            if v > freq_s[k]:
                return False
        return True