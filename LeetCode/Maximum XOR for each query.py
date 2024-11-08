from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        xor = 0
        for i in nums:
            xor ^= i

        mask = (1 << maximumBit) - 1

        for n in reversed(nums):
            answer.append(xor ^ mask)
            xor ^= n

        return answer