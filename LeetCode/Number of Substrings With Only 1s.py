class Solution:
    def numSub(self, s: str) -> int:
        MOD = (10**9) + 7

        n = len(s)
        total = 0
        consecutive = 0

        ans = 0

        for num in s:
            if num == '0':
                total += (consecutive * (consecutive + 1)) // 2
                consecutive = 0

            else:
                consecutive += 1

        total += (consecutive * (consecutive + 1)) // 2
        return total % MOD