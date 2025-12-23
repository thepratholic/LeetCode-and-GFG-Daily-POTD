import heapq
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        ans = 0
        maxi = 0
        pq = []
        for start, end, val in events:

            while pq and pq[0][0] < start:
                _, prev_val = heapq.heappop(pq)
                maxi = max(maxi, prev_val)

            ans = max(ans, val + maxi)
            heapq.heappush(pq, (end, val))

        return ans