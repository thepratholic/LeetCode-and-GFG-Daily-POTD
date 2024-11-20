class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        el1, el2 = -1, -1
        cnt1, cnt2 = 0, 0

        n = len(arr)

        for i in range(n):
            if cnt1 == 0 and arr[i] != el2:
                el1 = arr[i]
                cnt1 = 1

            elif cnt2 == 0 and arr[i] != el1:
                el2 = arr[i]
                cnt2 = 1

            elif arr[i] == el1: cnt1 += 1
            elif arr[i] == el2: cnt2 += 1

            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 =0, 0
        for i in range(n):
            if arr[i] == el1: cnt1 += 1
            if arr[i] == el2: cnt2 += 1
        res = []
        if cnt1 >= n//3 + 1: res.append(el1)
        if cnt2 >= n//3 + 1 and el1 != el2: res.append(el2)
        res.sort()
        return res