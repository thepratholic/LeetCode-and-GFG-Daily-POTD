from typing import List


class Solution:
    def subarrayBitwiseORs(self, nums: List[int]) -> int:
        n = len(nums)

        result = set()
        prev = set()

        for i in range(n):
            cur = set()
            for x in prev:
                cur.add(x | nums[i])
                result.add(x | nums[i])

            cur.add(nums[i])
            result.add(nums[i])
            prev = cur

        return len(result)