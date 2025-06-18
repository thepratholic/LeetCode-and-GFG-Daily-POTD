from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        ans = []
        n = len(nums)

        i = 0
        while i < n - 2:
            tmp = [nums[i], nums[i + 1], nums[i + 2]]

            if tmp[2] - tmp[0] > k:
                return []

            ans.append(tmp)
            i += 3

        return ans