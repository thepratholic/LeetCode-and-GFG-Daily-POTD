from typing import List


class Solution:
    def f(self, ranks, cars, mid):
        cnt = 0
        for r in ranks:
            cnt += int((mid // r) ** 0.5)
        return cnt >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, max(ranks) * cars * cars
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            if self.f(ranks, cars, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans 