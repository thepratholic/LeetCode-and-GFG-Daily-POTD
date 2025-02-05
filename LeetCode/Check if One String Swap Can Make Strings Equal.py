from collections import defaultdict
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        mpp = defaultdict(int)
        num_diff = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                num_diff += 1

            if num_diff > 2: return False

            mpp[s1[i]] += 1
            mpp[s2[i]] -= 1

        for k in mpp.values():
            if k != 0: return False

        return True