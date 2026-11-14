class Solution:
    def trap(self, height: List[int]) -> int:
        left = self.f(height)
        right = self.f(height[::-1])[::-1]
        ans = 0

        for i in range(len(height)):
            ans += max(0, min(left[i], right[i]) - height[i])
        return ans

    def f(self, nums):
        ans = []
        max_so_far = 0

        for i, n in enumerate(nums):
            ans.append(max_so_far)
            max_so_far = max(max_so_far, n)
        
        return ans
        
# At index i
# Tallest block on its left
# Tallest block on its right
# Minimum of this
# Subtract the height at index i

# Forward pass
# Keep track of the tallest block we have seen so far

# height:   [0 2 0 3 1 0 1 3 2 1]
# left:     [0 0 2 2 3 3 3 3 3 3]
# right:    [3 3 3 3 3 3 3 2 1 0]
# min:      [0 0 2 2 3 3 3 2 1 0]
# subtract: [0 0 2 0 2 3 2 0 0 0] 