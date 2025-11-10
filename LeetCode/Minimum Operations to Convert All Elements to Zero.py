from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        stack = []

        for i in range(n):

            while stack and stack[-1] > nums[i]:
                stack.pop()

            if nums[i] == 0:
                continue

            if (not stack) or (nums[i] > stack[-1]):
                ops += 1
                stack.append(nums[i])

        return ops