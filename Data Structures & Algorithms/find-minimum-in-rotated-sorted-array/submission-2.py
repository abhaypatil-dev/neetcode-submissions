class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L < R:
            i = (L + R) // 2
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                return nums[i + 1]
            else:
                if nums[i] > nums[0]:
                    L = i + 1
                else:
                    R = i

        return nums[0]