class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)

        stack = []
        ops = 0
        prev_ones = 0

        for ch in s:
            cur_ones = 0

            if ch == '0':
                if stack and stack[-1] == '1':
                    while stack and stack[-1] == '1':
                        cur_ones += 1
                        ops += 1
                        stack.pop()

                    ops += prev_ones
                    prev_ones += cur_ones

            stack.append(ch)

        return ops