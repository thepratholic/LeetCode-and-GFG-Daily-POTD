from typing import DefaultDict


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            freq = DefaultDict(int)

            for j in range(i, n):
                freq[s[j]] += 1

                if len(set(freq.values())) == 1:
                    ans = max(ans, j - i + 1)

        return ans