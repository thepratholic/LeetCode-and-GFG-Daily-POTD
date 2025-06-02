from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        sum = 1
        i = 1

        while i < n:
            if ratings[i] == ratings[i-1]:
                sum += 1
                i += 1
                continue

            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                sum += peak
                i += 1

            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                sum += down
                down += 1
                i += 1

            if down > peak:
                sum += (down - peak)

        return sum