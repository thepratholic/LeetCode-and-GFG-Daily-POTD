class Solution:
	def isWordExist(self, mat, word):
		n = len(mat)
		m = len(mat[0])
		
		def f(i, j, idx):
		    if i < 0 or j < 0 or i >= n or j >= m:
		        return False
		        
		    if mat[i][j] != word[idx]:
		        return False
		        
		    if idx == len(word) - 1:
		        return True
		    
		    tmp = mat[i][j] 
		    mat[i][j] = '.'
		    
		    if f(i - 1, j, idx + 1) or f(i, j - 1, idx + 1) or f(i + 1, j, idx + 1) or f(i, j + 1, idx + 1):
		        mat[i][j] = tmp
		        return True
		        
		    else:
		        mat[i][j] = tmp
		        
		    return False
		    
		
		for i in range(n):
		    for j in range(m):
		        if mat[i][j] == word[0]:
		            if f(i, j, 0):
		                return True
		                
		return False