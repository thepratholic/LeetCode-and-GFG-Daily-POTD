from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        grid = [[int(c) for c in row] for row in matrix]

        for j in range(m):
            for i in range(1, n):
                if grid[i][j] == 1: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] = 0


        def f(nums):
            stack = []
            sz = len(nums)
            res = 0
            for i in range(sz):
                while stack and nums[stack[-1]] >= nums[i]:
                    element = stack[-1]
                    stack.pop()
                    nse = i
                    pse = stack[-1] if stack else -1
                    res = max(res, nums[element] * (nse - pse - 1))

                stack.append(i)

            while stack:
                element = stack[-1]
                stack.pop()
                nse = sz
                pse = stack[-1] if stack else -1
                res = max(res, nums[element] * (nse - pse - 1))

            return res
        
        ans = float('-inf')
        for row in grid:
            ans = max(ans, f(row))

        return ans