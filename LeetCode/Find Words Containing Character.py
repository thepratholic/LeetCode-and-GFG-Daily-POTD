from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)

        ans = []

        for i in range(n):
            word = words[i]
            if x in word:
                ans.append(i)


        return ans