from collections import defaultdict
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        mpp = defaultdict(int)
        for i in nums:
            mpp[i] += 1

        ops = 0

        for e in mpp.keys():
            if e > k:
                ops += 1
            
            if e < k:
                return -1

        return ops