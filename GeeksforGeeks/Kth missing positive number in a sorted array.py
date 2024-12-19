class Solution:
    def kthMissing(self, arr, k):
        # code here

        n = len(arr)

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            miss = arr[mid] - (mid + 1)

            if miss < k:
                low = mid + 1

            else:
                high = mid - 1

        return low + k