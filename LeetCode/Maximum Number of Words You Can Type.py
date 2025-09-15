class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()

        ans = 0

        for word in words:
            f = True
            for ch in brokenLetters:
                if ch in word:
                    f = False
            if f:
                ans += 1

        return ans