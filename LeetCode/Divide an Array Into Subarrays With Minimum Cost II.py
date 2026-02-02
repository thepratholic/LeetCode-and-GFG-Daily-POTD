from bisect import bisect_left, insort
from typing import List


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        k_min = []
        remaining = []

        sum_k = 0
        i = 1

        while i - dist < 1:
            pair = (nums[i], i)
            sum_k += nums[i]
            insort(k_min, pair)

            if len(k_min) > k - 1:
                remove = k_min.pop()
                sum_k -= remove[0]
                insort(remaining, remove)

            i += 1

        res = float('inf')
        while i < n:
            pair = (nums[i], i)
            sum_k += nums[i]
            insort(k_min, pair)

            if len(k_min) > k - 1:
                temp = k_min.pop()
                sum_k -= temp[0]
                insort(remaining, temp)

            res = min(res, sum_k)

            remove = (nums[i - dist], i - dist)
            pos = bisect_left(k_min, remove)

            if pos < len(k_min) and k_min[pos] == remove:
                k_min.pop(pos)
                sum_k -= remove[0]

                if remaining:
                    temp = remaining.pop(0)
                    insort(k_min, temp)
                    sum_k += temp[0]

            else:
                pos = bisect_left(remaining, remove)
                if pos < len(remaining) and remaining[pos] == remove:
                    remaining.pop(pos)

            i += 1

        return nums[0] + res                    
