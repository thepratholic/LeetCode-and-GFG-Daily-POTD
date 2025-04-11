class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            if n % 2 == 1:
                continue
            half = n // 2
            left_sum = sum(int(d) for d in s[:half])
            right_sum = sum(int(d) for d in s[half:])
            if left_sum == right_sum:
                res += 1
        return res