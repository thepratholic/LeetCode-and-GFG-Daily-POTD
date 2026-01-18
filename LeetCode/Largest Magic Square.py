class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        row = [[0]*n for _ in range(m)]
        col = [[0]*n for _ in range(m)]
        diag1 = [[0]*n for _ in range(m)]
        diag2 = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row[i][j] = grid[i][j] + (row[i][j-1] if j > 0 else 0)
                col[i][j] = grid[i][j] + (col[i-1][j] if i > 0 else 0)
                diag1[i][j] = grid[i][j] + (diag1[i-1][j-1] if i > 0 and j > 0 else 0)
                diag2[i][j] = grid[i][j] + (diag2[i-1][j+1] if i > 0 and j+1 < n else 0)

        def rowSum(r, c1, c2):
            return row[r][c2] - (row[r][c1-1] if c1 > 0 else 0)

        def colSum(c, r1, r2):
            return col[r2][c] - (col[r1-1][c] if r1 > 0 else 0)

        def isMagic(r, c, k):
            target = rowSum(r, c, c+k-1)

            for i in range(k):
                if rowSum(r+i, c, c+k-1) != target:
                    return False

            for j in range(k):
                if colSum(c+j, r, r+k-1) != target:
                    return False

            d1 = diag1[r+k-1][c+k-1] - (diag1[r-1][c-1] if r > 0 and c > 0 else 0)
            if d1 != target:
                return False

            d2 = diag2[r+k-1][c] - (diag2[r-1][c+k] if r > 0 and c+k < n else 0)
            if d2 != target:
                return False

            return True

        for k in range(min(m, n), 1, -1):
            for r in range(m-k+1):
                for c in range(n-k+1):
                    if isMagic(r, c, k):
                        return k

        return 1
