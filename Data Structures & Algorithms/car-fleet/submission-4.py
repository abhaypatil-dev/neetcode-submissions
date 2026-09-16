class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        times = [(target - p) / s for p, s in zip(position, speed)]

        ans = 0
        fleet_time = 0

        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleet_time:
                ans += 1
                fleet_time = times[i]

        return ans

# times = [10, 4.5, 3, 3]
