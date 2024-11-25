class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		n = len(arr)
		pre = suf = 1
		ans = 0
		for i in range(n):
			if arr[i] < 0 and n == 1: return arr[i]
			if pre == 0: pre = 1
			if suf == 0: suf = 1
			pre *= arr[i]
			suf *= arr[n - i - 1]
			ans = max(ans, max(pre, suf))
		return ans