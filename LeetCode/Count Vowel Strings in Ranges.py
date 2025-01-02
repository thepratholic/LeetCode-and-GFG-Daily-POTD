from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}

        n = len(words)
        prefix = [0] * (n + 1)
        i = 0
        for i in range(n):
            if (words[i][0] in vowels and words[i][-1] in vowels):
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        ans = []
        for li, ri in queries:
            ans.append(prefix[ri + 1] - prefix[li])

        return ans