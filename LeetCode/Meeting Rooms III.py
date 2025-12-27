import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, a: List[List[int]]) -> int:
        a.sort()

        available = []
        for i in range(n):
            heapq.heappush(available, i)

        busy = [] # (end_time, roomNo) 
        most_used = [0] * n

        for s, e in a:
            d = e - s

            while busy and busy[0][0] <= s:
                end, roomNo = heapq.heappop(busy)
                heapq.heappush(available, roomNo)

            if available:
                room = heapq.heappop(available)
                most_used[room] += 1
                heapq.heappush(busy, (e, room))

            else:
                will_early_end_meeting, room = heapq.heappop(busy)
                new_d = d + will_early_end_meeting
                heapq.heappush(busy, (new_d, room))
                most_used[room] += 1

        maxi = max(most_used)
        for i, v in enumerate(most_used):
            if v == maxi:
                return i