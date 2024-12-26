from collections import defaultdict
class Solution:
	def twoSum(self, arr, target):
            d=defaultdict(int)
            for ind, ele in enumerate(arr):
                find=target-ele
                if find in d and d[find]!=ind:
                    return True
                d[ele]=ind
            return False