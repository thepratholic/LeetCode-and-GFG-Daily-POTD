from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        v = [0] * 100

        res = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a

            num = (a * 10) + b

            res += v[num]
            v[num] += 1

        return res 