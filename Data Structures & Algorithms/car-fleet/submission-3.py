class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        times = [(target - p)/s for p, s in zip(position, speed)]

        ans = 0
        fleet_time = 0

        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleet_time:
                ans += 1
                fleet_time = times[i]

        return ans



# position: [0 1 4 7]
# speed:    [1 2 2 1]
# time:     [10 4 3 3]

# 0 1 2 3 4 5 6 7 8 9 10
# o o     o     o     x
# 1 2     2     1

# slower car behind a faster car -> count as a fleet
# same speed behind same speed -> count as a fleet
# faster car behind slower car -> depends

# faster cannot catch up in time -> count as a fleet
# faster can catch up -> merge