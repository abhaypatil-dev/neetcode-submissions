class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        L = 0
        ans = 0

        for i in range(len(s)):
            freq[s[i]] += 1

            # shrink window until valid
            while (i - L + 1) - max([0] + list(freq.values())) > k:
                freq[s[L]] -= 1
                L += 1

            # print(L, i)
            ans = max(ans, i - L + 1)
        
        return ans

# AAABABB
# L   i