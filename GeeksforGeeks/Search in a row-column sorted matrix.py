#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		n, m = len(mat), len(mat[0])

        #User function Template for python3
class Solution:
	def matSearch(self, mat, x):

            # Complete this function
            n, m = len(mat), len(mat[0])
            i, j = 0, m - 1  # Start from the top-right corner

            while i < n and j >= 0:
                if mat[i][j] == x:
                    return True  # Element found
                elif mat[i][j] > x:
                    j -= 1  # Move left
                else:
                    i += 1  # Move down

            return False