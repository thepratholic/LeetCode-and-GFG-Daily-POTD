from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()

        n = len(words)
        for i in range(n):
            for j in range(n):
                if words[j] in words[i] and i != j:
                    ans.add(words[j])

        ans = list(ans)
        return ans