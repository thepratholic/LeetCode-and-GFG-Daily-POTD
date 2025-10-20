from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0

        n = len(operations)

        for i in range(n):
            operation = operations[i]

            if operation[0] == '-' or operation[-1] == '-':
                ans -= 1

            elif operation[0] == '+' or operation[-1] == '+':
                ans += 1

        return ans