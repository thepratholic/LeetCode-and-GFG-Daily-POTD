from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())

        ans = float("inf")

        n = len(freq)
        for i in range(n):
            base = freq[i]

            ops = 0
            for f in freq:
                if f < base:
                    ops += f

                elif f > base + k:
                    ops += f - (base + k)

            ans = min(ans, ops)

        return ans