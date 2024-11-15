class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        largest, secondLargest = arr[0], -1

        for i in range(n):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > secondLargest:
                secondLargest = arr[i]

        return secondLargest