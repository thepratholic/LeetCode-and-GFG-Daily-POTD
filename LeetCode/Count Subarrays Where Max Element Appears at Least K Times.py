from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)
        l, r = 0, 0
        count_of_maximum = 0
        ans = 0

        while r < n:
            if nums[r] == max_element:
                count_of_maximum += 1

            while count_of_maximum == k:
                if nums[l] == max_element:
                    count_of_maximum -= 1
                l += 1

            ans += l
            r += 1
        return ans
            