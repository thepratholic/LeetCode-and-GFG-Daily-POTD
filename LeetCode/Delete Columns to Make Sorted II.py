from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        already_sorted = [False] * (n - 1)

        ans = 0

        for j in range(m):

            deleted = False
            for i in range(n - 1):
                if not already_sorted[i] and strs[i][j] > strs[i + 1][j]:
                    deleted = True
                    break

            if deleted:
                ans += 1

            else:
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        already_sorted[i] = True

        return ans