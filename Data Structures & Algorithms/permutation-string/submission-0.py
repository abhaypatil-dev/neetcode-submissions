class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # frequeny count of s1: O(N)
        counts_s1 = defaultdict(int)
        for ch in s1:
            counts_s1[ch] += 1
        print(f"Counts s1: {counts_s1}")

        # sliding window fixed length over s2: O(N)
        counts = defaultdict(int)
        for i in range(len(s2)):
            counts[s2[i]] += 1
            if i - len(s1) >= 0:
                ch = s2[i - len(s1)]
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
            
            if counts == counts_s1:
                return True
        
        return False
