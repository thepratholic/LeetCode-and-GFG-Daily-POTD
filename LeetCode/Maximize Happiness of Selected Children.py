import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)

        pq = [] # max_heap

        for x in happiness:
            heapq.heappush(pq, -x)

        ans = 0
        dec = 0

        while k > 0:
            cur_val = heapq.heappop(pq)
            cur_val = -cur_val
            cur_val = max(0, cur_val - dec)

            ans += cur_val
            dec += 1
            k -= 1

        return ans