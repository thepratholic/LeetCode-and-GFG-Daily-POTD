class Solution:
    def is_match(self, stack, part_len, part):
        return "".join(stack[-part_len : ]) == part

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        part_len = len(part)

        for i in s:
            stack.append(i)

            if len(stack) >= part_len and self.is_match(stack, part_len, part):
                for _ in range(part_len):
                    stack.pop()

        return "".join(stack)