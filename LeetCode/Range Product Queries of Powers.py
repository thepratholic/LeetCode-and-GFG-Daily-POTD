from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        powers = []

        # I have seen this making powers array part from gpt, was unknown about it
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1

        answer = []
        prod = [-1] * len(powers)

        prod[0] = powers[0] % mod
        for i in range(1, len(powers)):
            prod[i] = (prod[i - 1] * powers[i]) % mod

        

        for l, r in queries:
            if l == 0:
                answer.append(prod[r])

            else:
                inv = pow(prod[l - 1], mod - 2, mod)
                answer.append((prod[r] * inv) % mod)

        return answer