class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        north = west = south = east = maxi = 0
        
        for i in range(n):
            if s[i] == "N": north += 1
            elif s[i] == "E": east += 1
            elif s[i] == "S": south += 1
            elif s[i] == "W": west += 1

            current_dist = abs(north - south) + abs(east - west)
            wasted_steps = (i + 1) -  current_dist

            extra = 0
            if wasted_steps != 0:
                extra = min(2 * k, wasted_steps)

            maxi = max(maxi, current_dist + extra)

        return maxi