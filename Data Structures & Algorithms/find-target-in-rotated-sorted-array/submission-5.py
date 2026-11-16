class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        if nums[-1] > nums[0]: return self.binarySearch(nums, target)

        while L <= R:
            i = (L + R) // 2

            if nums[i] == target: return i
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                if target < nums[0]:
                    res = self.binarySearch(nums[i + 1:], target)
                    return -1 if res == -1 else i + 1 + res
                else:
                    res = self.binarySearch(nums[:i + 1], target)
                    return -1 if res == -1 else res
            else:
                if nums[i] > nums[0]:
                    L = i + 1
                else:
                    R = i - 1
            
        return -1


    def binarySearch(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R:
            i = (L + R) // 2
            if nums[i] == target: return i
            elif nums[i] > target: R = i - 1
            else: L = i + 1
        return -1