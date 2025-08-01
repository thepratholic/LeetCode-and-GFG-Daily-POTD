from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        if numRows > 1:
            result.append([1, 1])

        for i in range(2, numRows):
            v = [1]

            for j in range(1, i):
                val = result[i - 1][j - 1] + result[i - 1][j]
                v.append(val)

            v.append(1)
            result.append(v)

        return result