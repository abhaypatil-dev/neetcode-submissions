class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)
        for chs, cht in zip(s, t):
            freq[chs] += 1
            freq[cht] -= 1
        
        return all(f == 0 for f in freq.values())