class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 

            # code here 
            
            n, m = len(mat), len(mat[0])
            row, col = 0, m - 1
            
            while row < n and col >= 0:
                if mat[row][col] == x:
                    return True 
                elif mat[row][col] > x:
                    col -= 1 
                else:
                    row += 1 
            
            return False