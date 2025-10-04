from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        i = 0
        j = n - 1

        ans = float('-inf')

        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))

            if(height[i] < height[j]):
                i += 1

            else:
                j -= 1

        return ans