from typing import List


class Solution:
    def child1Fruits(self, fruits):
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
        return ans

    def child2Fruits(self, i, j, fruits, dp):
        n = len(fruits)
        if i >= len(fruits) or j < 0 or j >= len(fruits):
            return 0 

        if i == n - 1 and j == n - 1:
            return 0

        if i == j or i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        bottomLeft = fruits[i][j] + self.child2Fruits(i + 1, j - 1, fruits, dp)
        bottomDown = fruits[i][j] + self.child2Fruits(i + 1, j, fruits, dp)
        bottomRight = fruits[i][j] + self.child2Fruits(i + 1, j + 1, fruits, dp)

        dp[i][j] = max(bottomLeft, bottomDown, bottomRight)
        return dp[i][j]

    def child3Fruits(self, i, j, fruits, dp):
        n = len(fruits)
        if i < 0 or j >= len(fruits) or i >= len(fruits):
            return 0

        if i == n - 1 and j == n - 1:
            return 0

        if i == j or i < j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        upRight = fruits[i][j] + self.child3Fruits(i - 1, j + 1, fruits, dp)
        right = fruits[i][j] + self.child3Fruits(i, j + 1, fruits, dp)
        bottomRight = fruits[i][j] + self.child3Fruits(i + 1, j + 1, fruits, dp)

        dp[i][j] = max(upRight, right, bottomRight)
        return dp[i][j]

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        c1 = self.child1Fruits(fruits)

        dp2 = [[-1] * n for _ in range(n)]
        c2 = self.child2Fruits(0, n - 1, fruits, dp2)

        dp3 = [[-1] * n for _ in range(n)]
        c3 = self.child3Fruits(n - 1, 0, fruits, dp3)

        return c1 + c2 + c3