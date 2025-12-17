class Solution:
	def mergeOverlap(self, arr):
		
		ans = []
		n = len(arr)
		
		arr.sort(key = lambda x : (x[0], x[1]))
		
		ans.append(arr[0])
		
		for i in range(1, n):
		    if arr[i][0] <= ans[-1][-1]:
		        
		        if arr[i][1] <= ans[-1][-1]:
		            continue
		        
		        elif arr[i][1] > ans[-1][-1]:
		            ans[-1][-1] = arr[i][1]
		            
		    else:
		        ans.append(arr[i])
		        
		return ans