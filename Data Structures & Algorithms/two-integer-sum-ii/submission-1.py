class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L, R = 0, n - 1

        while True:
            total = numbers[L] + numbers[R]

            if total == target:
                return [L + 1, R + 1]
            if total < target:
                L += 1
            else:
                R -= 1