class Solution:
    def peakElement(self,arr):
        # Code here
        n = len(arr)

        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == n-1 or arr[mid] >= arr[mid+1]):
                return mid
            elif arr[mid] < arr[mid+1]: 
                low = mid + 1
            else:
                high = mid - 1
        return -1