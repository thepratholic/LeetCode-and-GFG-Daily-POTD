import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []

        count = 0
        j = 0

        for day in range(1, max_day + 1):
            while j < n and events[j][0] <= day:
                heapq.heappush(pq, events[j][1])
                j += 1

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                count += 1

        return count
            