class Solution:
    def findMin(self, arr):
        # Complete the function here

        n = len(arr)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[high]:
                low = mid + 1
            elif arr[mid] < arr[high]:
                high = mid
            else:
                high -= 1  # Reduce the search space when duplicates are encountered

        return arr[low]