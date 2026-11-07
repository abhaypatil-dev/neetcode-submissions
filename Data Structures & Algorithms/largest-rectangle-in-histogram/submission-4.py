class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = self.extend_left(heights)
        right = self.extend_right(heights)

        # print(left)
        # print(right)

        ans = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            ans = max(ans, width * heights[i])
        return ans

    def extend_left(self, heights):
        n = len(heights)
        stack = []
        ans = []

        for i in range(n):
            index = i
            while stack and heights[i] <= heights[stack[-1][0]]:
                _, index = stack.pop()

            ans.append(index) 
            stack.append((i, index))
        
        return ans

    def extend_right(self, heights):
        n = len(heights)
        stack = []
        ans = []

        for i in range(n - 1, -1, -1):
            index = i
            while stack and heights[i] <= heights[stack[-1][0]]:
                _, index = stack.pop()

            ans.append(index) 
            stack.append((i, index))
        
        return ans[::-1]

# Left:  [0, 0, 2, 2, 2, 5]
# Right: [0, 5, 2, 5, 5, 5]
# Width: [1, 6, 1, 4, 4, 1] 