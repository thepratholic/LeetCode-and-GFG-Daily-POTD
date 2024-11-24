
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        summ = 0
        n = len(arr)
        maxi = float("-inf")

        for i in range(n):
            summ += arr[i]

            maxi = max(maxi, summ)
            if summ < 0: summ = 0

        return maxi
