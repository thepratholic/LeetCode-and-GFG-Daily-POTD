class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        minCharToRight = [''] * n
        minCharToRight[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            minCharToRight[i] = min(minCharToRight[i + 1], s[i])

        t = []
        paper = []

        for i in range(n):
            t.append(s[i])

            min_char =  minCharToRight[i + 1] if i + 1 < n else s[i]

            while t and t[-1] <= min_char:
                paper.append(t.pop())

        while t:
            paper.append(t.pop())

        return "".join(paper)