class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        if n < 3:
            return False

        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] in arr:
                    return True

        return False