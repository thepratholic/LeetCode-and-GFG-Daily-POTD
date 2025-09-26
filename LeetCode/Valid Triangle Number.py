from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        if n <  3:
            return 0

        nums.sort()
        ans = 0
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1

        return ans