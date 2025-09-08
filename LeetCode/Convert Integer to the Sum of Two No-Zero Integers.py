from typing import List


class Solution:
    def isValid(self, num):
        temp = num
        while temp > 0:
            ld = temp % 10
            if ld == 0:
                return False
            temp //= 10
        return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []

        for i in range(1, n + 1):

            for j in range(i, n + 1):
                fl = False

                if self.isValid(i) and self.isValid(j) and i + j == n:
                    fl = True
                    ans.extend([i, j])
                    break

            if fl:
                break

        return ans