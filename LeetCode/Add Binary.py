class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        ans = ['0'] * n

        carry = False
        for i in range(n - 1, -1, -1):
            ones = 0

            if a[i] == '1':
                ones += 1

            if b[i] == '1':
                ones += 1

            if carry:
                ones += 1

            if ones & 1:
                ans[i] = '1'

            carry = ones >= 2

        if carry:
            ans = ['1'] + ans

        return "".join(ans)