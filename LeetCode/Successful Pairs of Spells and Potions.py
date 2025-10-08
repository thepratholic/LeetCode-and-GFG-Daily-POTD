from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        potions.sort()

        def check(idx):
            ans = -1
            low, high = 0, m - 1

            while low <= high:
                mid = (low + high) >> 1

                if potions[mid] * spells[idx] >= success:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans if ans != -1 else m

        pairs = [-1] * n

        for i in range(n):
            pairs[i] = m - check(i)

        return pairs