class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for i, n in enumerate(nums):
            if n in candidates:
                return [candidates[n], i]
            candidates[target - n] = i