#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        
        slow, fast = head,head
        
        for i in range(n):
            fast = fast.next
            
        summ = 0
        
        while fast is not None:
            # summ += slow.data
            fast = fast.next
            slow = slow.next
            
        while slow != fast:
            summ += slow.data
            slow = slow.next
           
        return summ