class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        def f(x, n):
            res, mul = 1, x

            while n > 0:
                if n % 2 == 1:
                    res = res * mul % MOD
                mul = mul * mul % MOD
                n //= 2

            return res

        return f(5, (n + 1) // 2) * f(4, n // 2) % MOD