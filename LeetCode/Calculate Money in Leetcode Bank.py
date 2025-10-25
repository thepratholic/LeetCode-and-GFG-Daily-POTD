class Solution:
    def totalMoney(self, n: int) -> int:
        days = n

        week = 1
        ans = 0

        while days > 0:

            for money in range(week, week + 7):
                ans += money
                days -= 1
                if days == 0:
                    break

            week += 1

        return ans