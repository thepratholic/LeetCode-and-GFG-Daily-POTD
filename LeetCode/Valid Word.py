class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if not word or len(word) < 3:
            return False

        vowel = False
        consonant = False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if ch in vowels:
                    vowel = True

                else:
                    consonant = True

        return vowel and consonant