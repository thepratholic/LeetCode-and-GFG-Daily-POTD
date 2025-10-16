from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mpp = defaultdict(int)

        for num in nums:
            r = ((num % value) + value) % value

            mpp[r] += 1


        mex = 0

        while mpp[(mex % value)] > 0:
            mpp[(mex % value)] -= 1
            mex += 1

        return mex