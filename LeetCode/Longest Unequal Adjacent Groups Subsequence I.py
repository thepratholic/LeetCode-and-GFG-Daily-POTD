from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = []
        f = groups[0]
        ans.append(words[0])

        for i in range(n):
            if groups[i] != f:
                ans.append(words[i])
                f = groups[i]

        return ans