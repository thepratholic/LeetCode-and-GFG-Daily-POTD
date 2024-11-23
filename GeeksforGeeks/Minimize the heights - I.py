class Solution:
    def getMinDiff(self, k, arr):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)

        # Step 2: Initialize the result as the difference between max and min in the sorted array
        ans = arr[-1] - arr[0]

        # Step 3: Traverse through the array and adjust the heights
        for i in range(1, n):
            # The smallest and largest heights after the adjustment
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[-1] - k, arr[i-1] + k)

            # Update the answer with the minimum difference
            ans = min(ans, max_height - min_height)

        return ans