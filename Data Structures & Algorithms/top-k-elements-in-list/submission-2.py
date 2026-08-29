class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build freqdict: O(N)
        fd = defaultdict(int)
        for n in nums:
            fd[n] += 1

        # Bucket sort
        buckets = [[] for _ in range(len(nums))]

        for n, f in fd.items():
            buckets[f - 1].append(n)

        # Buckets
        # 0: 3
        # 1: 2
        # 2: 1
        # print(f"Buckets: {buckets}")

        # Get answer
        ans = []
        lst = []
        while k:
            while not lst:
                lst = buckets.pop()
            ans.append(lst.pop())
            k -= 1
        return ans