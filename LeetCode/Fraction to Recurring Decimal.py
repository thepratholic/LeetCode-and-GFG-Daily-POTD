class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0:
            return str(n // d)

        ans = []
        if (n < 0) ^ (d < 0):
            ans.append("-")

        n, d = abs(n), abs(d)

        ans.append(str(n // d))
        ans.append(".")

        r = n % d
        mpp = {}

        while r != 0:
            if r in mpp.keys():
                idx = mpp[r]
                ans.insert(idx, "(")
                ans.append(")")
                break

            mpp[r] = len(ans)
            r *= 10
            ans.append(str(r // d))
            r %= d
        return "".join(ans)