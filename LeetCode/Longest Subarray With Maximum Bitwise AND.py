class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi = max(nums)
        longest, current = float('-inf'), 0

        for element in nums:
            if element == maxi:
                current += 1
                longest = max(longest, current)

            else:
                current = 0

        return longest