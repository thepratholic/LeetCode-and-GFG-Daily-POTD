class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)

        stack = []

        for i in range(n):
            if s[i].isalpha():
                stack.append(s[i])

            elif s[i].isdigit():
                if stack:
                    stack.pop()

        return "".join(stack) if stack else ""