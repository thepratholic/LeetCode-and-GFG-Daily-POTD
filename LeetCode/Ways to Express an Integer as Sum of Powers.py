mod = 10 ** 9 + 7
class Solution:
    def f(self, n, cur_num, x, dp):
        if n == 0:
            return 1

        if n < 0:
            return 0


        currentPowerVal = cur_num ** x
        if currentPowerVal > n:
            return 0
        
        if dp[n][cur_num] != -1:
            return dp[n][cur_num]
            
        pick = self.f(n - currentPowerVal, cur_num + 1, x, dp)
        notPick = self.f(n, cur_num + 1, x, dp)

        dp[n][cur_num] = (notPick + pick) % mod
        return dp[n][cur_num]

    def numberOfWays(self, n: int, x: int) -> int:
        
        dp = [[-1] * (301) for _ in range(301)]
        return self.f(n, 1, x, dp)
        