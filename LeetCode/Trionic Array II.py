from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        left = [0] * n
        left[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = max(nums[i], left[i - 1] + nums[i])

            else:
                left[i] = nums[i]

            
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = max(nums[i], right[i + 1] + nums[i])
            else:
                right[i] = nums[i]

        ans = float('-inf')
        i = 0

        while i < n:

            if i + 2 < n and nums[i] < nums[i + 1] > nums[i + 2]:
                # it means humko decreasing part mil gaya hai so, ab uss part ko calculate karo
                j = i + 1

                mid_sum = 0

                while j + 1 < n and nums[j] > nums[j + 1]:
                    mid_sum += nums[j]
                    j += 1

                mid_sum += nums[j]

                if j + 1 < n and nums[j] < nums[j + 1]:
                    # yeh condition last increasing ko check kr rhi hai, so like if yes then ans calc karo
                    ans = max(ans, left[i] + mid_sum + right[j + 1])

                i = j - 1

            i += 1

        return ans