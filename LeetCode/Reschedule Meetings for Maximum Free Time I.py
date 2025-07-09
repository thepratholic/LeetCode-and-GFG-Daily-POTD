from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_times = []
        ans = 0
        n = len(startTime)

        free_times.append(startTime[0] - 0)

        for i in range(1, n):
            free_times.append(startTime[i] - endTime[i-1])

        free_times.append(eventTime - endTime[-1])
        
        l, r = 0, 0
        maxi = float('-inf')

        cur = 0
        while r < len(free_times):
            cur += free_times[r]

            if r - l + 1 > k + 1:
                while r - l + 1 > k + 1:
                    cur -= free_times[l]
                    l += 1

            maxi = max(maxi, cur)
            r += 1

        return maxi 