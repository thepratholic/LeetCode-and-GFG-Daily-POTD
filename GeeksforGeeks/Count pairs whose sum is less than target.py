class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here

        n = len(arr)
        arr.sort()
        cnt = 0
        l, r = 0, n - 1

        while l < r:
            s = arr[l] + arr[r]

            if s < target:
                cnt += (r - l)
                l += 1
            else:
                r-=1

        return cnt