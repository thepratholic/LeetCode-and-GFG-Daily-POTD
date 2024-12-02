
class Solution:
    def search(self, pat, txt):
        # code here

        n = len(txt)
        m = len(pat)
        indices = []


        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                indices.append(i)

        return indices