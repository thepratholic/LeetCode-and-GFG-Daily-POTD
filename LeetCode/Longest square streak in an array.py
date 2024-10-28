from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streaks = {}

        nums.sort()

        for num in nums:
            root = int(num ** 0.5)

            if root * root == num and root in streaks:
                streaks[num] = streaks[root] + 1
            else:
                streaks[num] = 1

        longestStreak = max(streaks.values(), default=0)

        return longestStreak if longestStreak > 1 else -1
