class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        leftClosestR = [-1] * n
        rightClosestL = [-1] * n
        result = [-1] * n

        # finding the indices of left closest R
        for i in range(n):
            if dominoes[i] == 'R':
                leftClosestR[i] = i
            elif dominoes[i] == '.':
                leftClosestR[i] = leftClosestR[i - 1] if i > 0 else -1

        
        # finding the indices of right closest L
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                rightClosestL[i] = i
            elif dominoes[i] == '.':
                rightClosestL[i] = rightClosestL[i + 1] if i < n - 1 else -1

        for i in range(n):
            distRightL = abs(i - rightClosestL[i])
            distLeftR = abs(i - leftClosestR[i])

            if rightClosestL[i] == leftClosestR[i]:
                result[i] = '.'

            elif leftClosestR[i] == -1:
                result[i] = 'L'

            elif rightClosestL[i] == -1:
                result[i] = 'R'

            elif distRightL == distLeftR:
                result[i] = '.'

            else:
                result[i] = 'L' if distLeftR > distRightL else 'R'

        return "".join(result)