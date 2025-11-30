from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        t = sum(nums) % p

        if t == 0:
            return 0

        mpp = {0 : -1}
        cur = 0
        ans = n
        for i in range(n):

            cur = (cur + nums[i]) % p

            prev = (cur - t + p) % p

            if prev in mpp:
                ans = min(ans, i - mpp[prev])

            mpp[cur] = i

        return ans if ans != n else -1