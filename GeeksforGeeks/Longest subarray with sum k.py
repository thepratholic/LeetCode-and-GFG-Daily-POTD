class Solution:
    def longestSubarray(self, arr, k):
        # code here

        mpp = {}
        longest = 0

        s = 0

        n = len(arr)

        for i in range(n):

            s += arr[i]

            if s == k:
                longest = max(longest, i+1)

            rem = s - k

            if rem in mpp:
                longest = max(longest, i - mpp[rem])

            if s not in mpp:
                mpp[s] = i

        return longest