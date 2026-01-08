from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        NEG = -10 ** 18

        def f(i, j):
            if i == n or j == m:
                return NEG

            if dp[i][j] != -1:
                return dp[i][j]

            take_both = nums1[i] * nums2[j] + max(0, f(i + 1, j + 1))

            skip1 = f(i + 1, j)
            skip2 = f(i, j + 1)

            dp[i][j] = max(take_both, skip1, skip2)
            return dp[i][j]

        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return f(0, 0)