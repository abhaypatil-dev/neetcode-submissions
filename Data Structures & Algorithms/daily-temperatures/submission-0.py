class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack (temp, index)
        stack = []
        ans = []
        
        # for t in temps rev
        for i in range(len(temperatures) - 1, -1, -1):
            # t will pop out the colder temps in the stack
            t = temperatures[i]
            while stack and t >= stack[-1][0]:
                stack.pop()

            if stack:
                # diff = stack top index - current index
                diff = stack[-1][1] - i
                ans.append(diff)
            else:
                ans.append(0)

            # stack append t
            stack.append((t, i))

        # reverse ans and return
        return ans[::-1]

