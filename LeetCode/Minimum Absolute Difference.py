from typing import List


class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        mini = float('inf')
        for i in range(1, n):
            mini = min(mini, nums[i] - nums[i - 1])

        ans = []
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == mini:
                ans.append([nums[i], nums[i + 1]])

        return ans