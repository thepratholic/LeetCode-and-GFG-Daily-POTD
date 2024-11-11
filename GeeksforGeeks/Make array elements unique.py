class Solution:
    def minIncrements(self, arr):
        # Code here
        arr.sort()
        n = len(arr)
        inc = 0

        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                req_inc = arr[i - 1] + 1 - arr[i]
                arr[i] = arr[i-1] + 1
                inc += req_inc

        return inc