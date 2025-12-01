from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        low, high = min(batteries), sum(batteries) // n
        ans = 0

        def f(time):
            t = time * n # itna target minutes hai jo saare computers ko bana k milta hai
            s = 0

            for i in range(len(batteries)):
                s += min(batteries[i], time)
                if s >= t:
                    return True

            return s >= t

        while low <= high:
            mid = (low + high) >> 1

            if f(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans