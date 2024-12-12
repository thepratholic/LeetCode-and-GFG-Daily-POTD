class Solution:
    def countFreq(self, arr, target):
        #code here

        n = len(arr)
        cnt = 0
        for i in range(n):
            if arr[i] == target: cnt += 1

        return cnt