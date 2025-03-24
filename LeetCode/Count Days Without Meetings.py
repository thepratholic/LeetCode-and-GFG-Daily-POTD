from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free, prev_end = 0, 0

        for start, end in meetings:
            if start > prev_end + 1:
                free += start - prev_end - 1

            prev_end = max(prev_end, end)

        free += days - prev_end

        return free