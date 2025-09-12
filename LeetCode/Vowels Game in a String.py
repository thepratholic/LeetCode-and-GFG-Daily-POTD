class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        v = []

        for ch in s:
            if ch in vowels:
                v.append(ch)


        if not v:
            return False

        else:
            return True