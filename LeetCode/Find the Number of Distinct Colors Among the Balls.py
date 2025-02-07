from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = [-1] * n

        mpp = {}
        color_count = {}
        i = 0
        
        for i in range(n):
            x, y = queries[i][0], queries[i][1]

            if x in mpp:
                color = mpp[x]
                color_count[color] -= 1
                if color_count[color] == 0:
                    del color_count[color]

            mpp[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            result[i] = len(color_count)

        return result