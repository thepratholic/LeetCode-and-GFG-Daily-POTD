from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        ans = [1] * n

        dry_days = SortedList()
        last_rain = {}

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(i)
            else:

                if lake in last_rain:
                    prev = last_rain[lake]
                    idx = dry_days.bisect_right(prev)

                    if idx == len(dry_days):
                        return []

                    dry_day = dry_days[idx]

                    ans[dry_day] = lake
                    dry_days.remove(dry_day)

                last_rain[lake] = i
                ans[i] = -1

        return ans