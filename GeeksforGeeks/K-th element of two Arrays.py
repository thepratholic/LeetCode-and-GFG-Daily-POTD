class Solution:
    def kthElement(self, a, b, k):
        
        a.extend(b)
        a.sort()
        
        return a[k - 1]