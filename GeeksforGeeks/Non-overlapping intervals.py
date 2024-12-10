class Solution:
    def minRemoval(self, intervals):
        # Code here

        intervals = sorted(intervals, key=lambda x : x[1])

        end = intervals[0][1]
        cnt = 1

        n = len(intervals)

        for i in range(1, n):
            if intervals[i][0] >= end:
                cnt += 1
                end = intervals[i][1]
            else:
                continue

        return n - cnt