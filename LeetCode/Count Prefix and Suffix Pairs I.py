from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if s2.startswith(s1) and s2.endswith(s1):
                return True
            else:
                return False

        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                if isPrefixAndSuffix(words[i], words[j]) and i != j:
                    cnt += 1
        return cnt