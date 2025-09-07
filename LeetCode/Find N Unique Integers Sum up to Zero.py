from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        ans = []

        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)


        if n & 1:
            ans.append(0)

        return ans