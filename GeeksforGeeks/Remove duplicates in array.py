class Solution:
    def removeDuplicates(self, arr):
        # code here
        l = []

        for i in arr:
            if i not in l:
                l.append(i)
            else:
                continue

        return l