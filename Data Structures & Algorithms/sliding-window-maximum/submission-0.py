class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Build heap
        heap = [-n for n in nums[:k]]
        heapq.heapify(heap)

        # Build seen
        seen = defaultdict(int)
        for i in range(k):
            seen[nums[i]] += 1

        # Iterate
        ans = [-heap[0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, -nums[i])
            seen[nums[i]] += 1
            seen[nums[i - k]] -= 1

            while seen[-heap[0]] <= 0:
                heapq.heappop(heap)

            ans.append(-heap[0])

        return ans

# [1 2 1 0 0 0]
# ans = [2 2 1]
        
# For the first window, we find the max
# [1 2 1], Max=2
# As we move the window, we add a number, and remove a number


# -------------------------------------------------
# 1 2 1 0 0 4 2 3 0 6
# [1 2 1] = 2
# [2 1 0] = 2
# [1 0 0] = 1
# [0 0 4] = 4
# [0 4 2] = 4
# [4 2 3] = 4
# [2 3 0] = 3
# [3 0 6] = 6