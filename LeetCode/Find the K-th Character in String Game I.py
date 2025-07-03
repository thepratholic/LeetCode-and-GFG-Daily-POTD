class Solution:
    def kthCharacter(self, k: int) -> str:
        initial = "a"

        while len(initial) < k:
            temp = ""

            for ch in initial:
                next_ch = chr((ord(ch) - ord("a")) + 1 % 26 + ord("a"))
                temp += next_ch

            initial += temp

        return initial[k - 1]