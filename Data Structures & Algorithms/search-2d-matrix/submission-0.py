class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = self.getRow([matrix[r][0] for r in range(len(matrix))], target)
        nums = matrix[row_num]

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False
        
    def getRow(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return R

# 1 10 14