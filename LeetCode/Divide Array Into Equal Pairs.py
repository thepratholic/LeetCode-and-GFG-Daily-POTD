from collections import defaultdict
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mpp = defaultdict(int)

        for i in nums:
            mpp[i] += 1

        for k, v in mpp.items():
            if v % 2 == 1:
                return False

        return True