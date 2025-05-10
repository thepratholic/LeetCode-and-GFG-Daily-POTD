from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        sum_nums1 = sum(nums1) + z1
        sum_nums2 = sum(nums2) + z2

        if sum_nums1 < sum_nums2 and z1 == 0: return -1

        if sum_nums2 < sum_nums1 and z2 == 0: return -1

        return max(sum_nums1, sum_nums2)