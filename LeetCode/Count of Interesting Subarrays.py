from collections import defaultdict
from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        cur_cnt = 0
        
        for element in nums:
            if element % modulo == k:
                cur_cnt += 1

            target = (cur_cnt - k) % modulo

            if target in mpp:
                res += mpp[target]

            mpp[cur_cnt % modulo] += 1
        return res