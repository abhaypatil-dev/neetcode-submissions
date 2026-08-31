class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a b c d]
        # [1      a     ab   abc   abcd]
        # [abcd   bcd   cd    d     1  ]

        prefix = self.buildPrefix(nums)
        suffix = self.buildPrefix(nums[::-1])[::-1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i + 1])
        return ans

    def buildPrefix(self, nums):
        p = 1
        ans = [1]
        for n in nums:
            p *= n
            ans.append(p)
        return ans