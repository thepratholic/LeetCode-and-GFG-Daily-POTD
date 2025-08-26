import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        n = len(dim)
        ans = -1
        maxi = float('-inf')

        for l, w in dim:
            v = (l * l) + (w * w)
            area = l * w
            diag_length = math.sqrt(v)

            if diag_length > maxi:
                maxi = diag_length
                ans = l * w

            elif diag_length == maxi:
                ans = max(ans, area)
        return ans