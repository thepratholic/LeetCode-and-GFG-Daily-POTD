class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split()
        isCircular = True
        n = len(l)

        for i in range(n):
            if l[i][0] == l[i-1][-1]:
                pass
            else: isCircular = False

        if l[i][-1] == l[0][0]:
                pass
        else: isCircular = False
        return isCircular