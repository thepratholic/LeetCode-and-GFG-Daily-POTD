class Solution:

    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat):
        # code here

        n = len(mat)

        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


        for i in range(n//2):
            mat[i], mat[n-i-1] = mat[n-i-1], mat[i]

        return mat