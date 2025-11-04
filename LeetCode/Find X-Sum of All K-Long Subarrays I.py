from typing import Counter, List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        ans = []
        for i in range(n - k + 1):
            sub = nums[i : i + k]

            freq = Counter(sub)
            top = sorted(freq.items(), key = lambda z : (z[1], z[0]), reverse = True)

            if len(top) < x:
                ans.append(sum(sub))
            else:
                cur = 0
                for f, v in top[:x]:
                    cur += (f * v)

                ans.append(cur)

        return ans