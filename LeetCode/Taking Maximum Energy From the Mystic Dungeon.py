from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        maxi = float('-inf')
        dp = [0] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i] + 0

            maxi = max(maxi, dp[i])

        return maxi