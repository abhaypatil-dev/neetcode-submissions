class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        L, R = 0, N - 1
        ans = 0

        while L < R:
            width = R - L
            height = min(heights[L], heights[R])
            capacity = height * width
            ans = max(ans, capacity)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return ans
    
# to get the capacity of a container - we need the height and width
# width = j - i
# height = min(Hi, Hj)
