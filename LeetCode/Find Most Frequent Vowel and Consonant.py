from typing import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = Counter(s)
        max_vowel_freq = 0
        max_consonent_freq = 0

        for k, v in freq.items():
            if k in vowels:
                if v > max_vowel_freq:
                    max_vowel_freq = v

            else:
                if v > max_consonent_freq:
                    max_consonent_freq = v

        return max_consonent_freq + max_vowel_freq