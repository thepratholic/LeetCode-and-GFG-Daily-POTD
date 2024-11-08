class Solution:
    def computeLPSArray(self,pat):
        M = len(pat)
        lps = [0] * M
        length = 0
        i = 1

        while i < M:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:

                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def KMPSearch(self, txt, pat, lps):
        N = len(txt)
        M = len(pat)
        i = 0
        j = 0
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                return True

            elif i < N and pat[j] != txt[i]:

                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False


    def minRepeats(self, A, B):
        lenA = len(A)
        lenB = len(B)

        lps = self.computeLPSArray(B)

        X = (lenB + lenA - 1) // lenA

        newA = A * X

        if self.KMPSearch(newA, B, lps):
            return X

        newA += A
        if self.KMPSearch(newA, B, lps):
            return X + 1

        return -1
