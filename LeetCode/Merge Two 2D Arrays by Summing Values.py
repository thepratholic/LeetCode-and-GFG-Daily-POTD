from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        res = []
        ptr1, ptr2 = 0, 0

        while ptr1 < n and ptr2 < m:
            id1, id2 = nums1[ptr1][0], nums2[ptr2][0]
            val1, val2 = nums1[ptr1][1], nums2[ptr2][1]

            if id1 == id2:
                res.append([id1, val1 + val2])
                ptr1 += 1
                ptr2 += 1

            elif id1 < id2:
                res.append([id1, val1])
                ptr1 += 1

            else:
                res.append([id2, val2])
                ptr2 += 1

        
        while ptr1 < n:
            id1, val1 = nums1[ptr1][0], nums1[ptr1][1]
            res.append([id1, val1])
            ptr1 += 1

        while ptr2 < m:
            id2, val2 = nums2[ptr2][0], nums2[ptr2][1]
            res.append([id2, val2])
            ptr2 += 1

        return res
