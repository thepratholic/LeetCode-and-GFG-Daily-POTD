class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            s = self.f(s)
        return s

    def f(self, s):
        res = []

        prev = s[0]
        cnt = 1

        for ch in s[1:]:
            if ch == prev:
                cnt += 1

            else:
                res.append(str(cnt))
                res.append(prev)

                prev = ch
                cnt = 1

        res.append(str(cnt))
        res.append(prev)

        return "".join(res)
