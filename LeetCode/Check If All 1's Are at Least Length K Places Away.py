from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        ones = []
        for i in range(n):
            if nums[i] == 1:
                ones.append(i)

        if not ones or len(ones) == 1:
            return True

        for i in range(1, len(ones)):
            if ones[i] - ones[i - 1] <= k:
                return False

        return True