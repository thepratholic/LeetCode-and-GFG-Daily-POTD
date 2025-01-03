class Solution:
    def subarrayXor(self, arr, k):
        # code here

        mpp = {0:1}
        n = len(arr)
        cnt = 0
        xr = 0

        for i in range(n):
            xr ^= arr[i]
            x = xr ^ k
            cnt += mpp.get(x, 0)
            mpp[xr] = mpp.get(xr, 0) + 1

        return cnt