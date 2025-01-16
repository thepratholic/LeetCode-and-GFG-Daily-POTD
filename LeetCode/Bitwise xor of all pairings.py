from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0

        if len(nums2) % 2 == 1:
            for i in nums1:
                xor1 ^= i

        if len(nums1) % 2 == 1:
            for j in nums2:
                xor2 ^= j

        return xor1 ^ xor2