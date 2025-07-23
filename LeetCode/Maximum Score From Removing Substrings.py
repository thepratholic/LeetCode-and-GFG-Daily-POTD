class Solution:
    def helper(self, s, a, b, score):
        res = 0
        stack = []

        for ch in s:
            if stack and stack[-1] == a and ch == b:
                res += score
                stack.pop()

            else:
                stack.append(ch)

        return "".join(stack), res


    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x > y:
            s, score = self.helper(s, 'a', 'b', x)
            ans += score

            _, score = self.helper(s, 'b', 'a', y)
            ans += score

        else:
            s, score = self.helper(s, 'b', 'a', y)
            ans += score
            _, score = self.helper(s, 'a', 'b', x)
            ans += score

        return ans