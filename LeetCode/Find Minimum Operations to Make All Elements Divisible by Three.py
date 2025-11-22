from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0

        for i in range(n):
            if nums[i] == 1:
                ans += 1

            elif nums[i] % 3 != 0:
                a1, a2 = 0, 0
                tmp1 = nums[i]
                while tmp1 % 3 != 0:
                    tmp1 += 1
                    a1 += 1

                tmp2 = nums[i]
                while tmp2 % 3 != 0:
                    tmp2 -= 1
                    a2 += 1

                ans += min(a1, a2)


        return ans