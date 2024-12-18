class Solution:
    def f(self, arr, mid):
        cntStudents = 1
        pagesStudents = 0
        for i in range(len(arr)):
            if pagesStudents + arr[i] <= mid:
                pagesStudents += arr[i]
            else:
                cntStudents += 1
                pagesStudents = arr[i]

        return cntStudents
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if k > len(arr): return -1
        ans = -1
        low, high = max(arr), sum(arr)

        while low <= high:
            mid = (low + high) // 2

            if self.f(arr, mid) > k:
                low = mid + 1

            else:
                ans = mid
                high = mid - 1

        return ans