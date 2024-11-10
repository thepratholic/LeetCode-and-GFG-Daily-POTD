class Solution:
    def findUnion(self,a,b):

        n, m = len(a), len(b)
        union = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] <= b[j]:
                if not union or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            else:
                if not union or union[-1] != b[j]:
                    union.append(b[j])
                j += 1

        while i < n:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i += 1

        while j < m:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1

        return union