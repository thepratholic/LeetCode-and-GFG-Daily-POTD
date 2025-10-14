from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        first, second = False, False

        for i in range(n - 2 * k + 1):
            ptr = i + 1
            first = True
            while ptr < i + k:
                if nums[ptr] > nums[ptr - 1]:
                    ptr += 1
                else: 
                    first = False
                    break

            ptr = i + k + 1
            second = True
            while ptr < i + 2 * k:
                if nums[ptr] > nums[ptr - 1]:
                    ptr += 1
                else: 
                    second = False
                    break
                # ptr += 1

            if first and second:
                return True


        return False