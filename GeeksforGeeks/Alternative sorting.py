class Solution:
    def alternateSort(self,arr):
        # Your code goes here

        arr.sort()

        ans = []

        if len(arr) == 1:
            ans.append(arr[0])
            return ans

        ans.append(arr[-1])
        ans.append(arr[0])

        i, j = 1, len(arr) - 2

        while i <= j:
            if ans[-2] > arr[j] and ans[-1] < arr[j]:
                ans.append(arr[j])
                j-=1
            else:
                ans.append(arr[i])
                i+=1
        return ans