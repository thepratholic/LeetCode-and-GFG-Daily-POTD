class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        first_row_zero = False
        first_col_zero = False

        # Step 1: Use first row and column as markers
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    if i == 0: 
                        first_row_zero = True
                    if j == 0: 
                        first_col_zero = True
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Step 2: Set matrix zeroes based on markers (excluding the first row and column)
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Step 3: Handle the first row
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0

        # Step 4: Handle the first column
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0

        return mat