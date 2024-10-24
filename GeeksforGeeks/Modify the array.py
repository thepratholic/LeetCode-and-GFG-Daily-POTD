class Solution:
    def helper(self, arr):
        non_zero_index = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index+=1
        return arr
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        
        
        n = len(arr)
        ans = [-1] * n
        
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                arr[i-1] = arr[i-1] * 2
                arr[i] = 0
            else:
                continue
        self.helper(arr)
        return arr
            

s = Solution()
print(s.modifyAndRearrangeArr([2, 2, 0, 4, 0, 8]))