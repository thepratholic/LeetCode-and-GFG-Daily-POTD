from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] == 2:
                res.append(-1)
                continue

            found = False
            for bit in range(32):
                if nums[i] & (1 << bit) > 0:
                    continue

                prev = bit - 1
                x = nums[i] ^ (1 << (prev))
                res.append(x)
                found = True
                break

            if not found:
                res.append(-1)

        return res