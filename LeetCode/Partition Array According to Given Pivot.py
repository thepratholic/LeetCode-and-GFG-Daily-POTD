from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        n = len(nums)
        less, more = [], []

        for i in range(n):
            if nums[i] < pivot:
                less.append(nums[i])

            if nums[i] > pivot:
                more.append(nums[i])

        
        for i in range(n):
            if nums[i] == pivot:
                less.append(nums[i])
        

        res = []
        res.extend(less)
        res.extend(more)
        return res