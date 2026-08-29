class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Frequency dictionary - needs to be encoded
        # Build it as a tuple
        groups = defaultdict(list)

        for s in strs:
            fd = [0] * 26
            for ch in s:
                fd[ord(ch) - ord('a')] += 1
            
            groups[tuple(fd)].append(s)

        return list(groups.values())