class Solution:
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here

        union = set()

        for i in a:
            union.add(i)

        for j in b:
            if j not in union:
                union.add(j)

        union = list(union)
        return len(union)