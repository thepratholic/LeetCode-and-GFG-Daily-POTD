class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def merge(self, arr, low, mid, high):
        tmp, left, right = [], low, mid + 1
        cnt = 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                cnt += (mid - left + 1)
                right += 1

        while left <= mid:
            tmp.append(arr[left])
            left += 1

        while right <= high:
            tmp.append(arr[right])
            right += 1
        
        for i in range(low, high + 1):
            arr[i] = tmp[i - low]

        return cnt

    def mergeSort(self, arr, low, high):
        cnt = 0
        if low < high:
            mid = low + (high - low) // 2
            
            # Sort left half
            cnt += self.mergeSort(arr, low, mid)
            
            # Sort right half
            cnt += self.mergeSort(arr, mid + 1, high)
            
            # Merge and count inversions
            cnt += self.merge(arr, low, mid, high)
        return cnt
    def inversionCount(self, arr):
        # Your Code Here
        return self.mergeSort(arr, 0, len(arr) - 1)