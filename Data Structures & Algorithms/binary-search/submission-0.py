class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L, R = 0, N - 1

        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return -1