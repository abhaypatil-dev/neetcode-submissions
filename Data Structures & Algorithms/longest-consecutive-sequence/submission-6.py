class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 4 ... 5 6 ... 3
        # while (n + 1) exists, update
        # keep a set - processed, add to set in the loop

        # 4
        # 4:1 --- check for 5 --- present --- update
        # 4:2 --- check for 6 --- present --- update
        # 4:3 --- check for 7 --- abset   --- stop

        # 5
        # already in processed set, skip

        # 3
        # 3:1 --- check for 4 --- present --- update

        if not nums: return 0
        processed = set()
        seen = set(nums)
        marked = {n:1 for n in nums}

        for n in nums:
            if n in processed: continue
            processed.add(n)

            i = n + 1
            while i in seen:
                if marked[i] > 1:
                    marked[n] += marked[i]
                    break
                marked[n] += 1
                i += 1

        return max(marked.values())