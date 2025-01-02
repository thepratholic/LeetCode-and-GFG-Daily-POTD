class Solution:
    def countSubarrays(self, arr, k):
        # code here

        hashh = {0:1}
        cnt = 0
        s = 0

        n = len(arr)

        for i in range(n):
            s += arr[i]

            if s-k in hashh:
                cnt += hashh[s-k]

            hashh[s] = hashh.get(s, 0) + 1

        return cnt