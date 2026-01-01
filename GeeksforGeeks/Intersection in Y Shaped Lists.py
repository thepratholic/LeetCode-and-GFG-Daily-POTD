'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        
        t1 = head1
        t2 = head2
        
        while t1 != t2:
            t1 = t1.next if t1 else head2
            t2 = t2.next if t2 else head1
            
        return t1
        