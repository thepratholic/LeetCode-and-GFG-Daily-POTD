from bisect import bisect_left
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort(reverse = True)

        low, high = 0, min(n, m)

        def f(mid):
            pills_used = 0
            st = sorted(workers[:mid])
            for i in range(mid - 1, -1, -1):
                reqrd = tasks[i]
                if st[-1] >= reqrd:
                    st.pop() 
                elif pills_used >= pills:
                    return False
                else:
                    idx = bisect_left(st, reqrd - strength)
                    if idx == len(st):
                        return False
                    st.pop(idx)
                    pills_used += 1
            return True

        ans = 0
        while low <= high:
            mid = (low + high) >> 1

            if f(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans