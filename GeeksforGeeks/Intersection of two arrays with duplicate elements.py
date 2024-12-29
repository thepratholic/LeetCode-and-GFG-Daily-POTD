class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here

        intersection = set()
        a.sort()
        b.sort()

        i, j = 0, 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                i += 1

            elif b[j] < a[i]:
                j += 1

            else:
                intersection.add(a[i])
                i += 1
                j += 1

        intersection = list(intersection)
        return intersection