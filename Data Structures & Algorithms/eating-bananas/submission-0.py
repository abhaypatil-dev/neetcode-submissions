class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        while L < R:
            mid = (L + R) // 2
            if not self.canEat(piles, mid, h):
                L = mid + 1
            else:
                R = mid
        return R
        
    def canEat(self, piles, rate, h):
        hours = 0
        for p in piles:
            hours += math.ceil(p / rate)
        return hours <= h