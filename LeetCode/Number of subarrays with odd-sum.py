from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mpp = {0:1}
        MOD = 10**9 + 7
        cnt = 0
        s = 0
        for num in arr:
            s += num

            if s % 2 == 1:
                cnt += mpp.get(0, 0) % MOD
            else:
                cnt += mpp.get(1, 0) % MOD

            mpp[s % 2] = mpp.get(s % 2, 0) + 1

        return cnt % MOD