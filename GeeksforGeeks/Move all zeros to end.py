class Solution:
	def pushZerosToEnd(self,arr):
		j = -1
		n = len(arr)
		for i in range(n):
			if arr[i] == 0:
				j = i
				break
		if j == -1: return
		for i in range(j+1, n):
			if arr[i] != 0:
				arr[i], arr[j] = arr[j], arr[i]
				j += 1
		return arr