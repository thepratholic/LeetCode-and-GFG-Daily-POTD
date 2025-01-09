class Solution:
    def subarraySum(self, arr, target):
        # code here

        mpp = {}
        n = len(arr)

        ans = [-1, -1]

        s = 0

        for i in range(n):
            s += arr[i]

            if s == target:
                ans[0] = 1
                ans[1] = i+1
                return ans

            remove = s - target

            if remove in mpp:
                ans[0] = mpp[remove] + 1
                ans[1] = i + 1
                return ans

            if s not in mpp:
                mpp[s] = i+1

        return [-1]