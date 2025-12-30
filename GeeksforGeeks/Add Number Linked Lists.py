class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

import sys
sys.set_int_max_str_digits(1000000)


class Solution:
    def addTwoLists(self, head1, head2):
        
        t1 = head1
        num1 = 0
        
        while t1 is not None:
            num1 = (num1 * 10) + t1.data
            t1 = t1.next
            
        
        t2 = head2
        num2 = 0
        while t2 is not None:
            num2 = (num2 * 10) + t2.data
            t2 = t2.next
            
        total = num1 + num2
        
        total = str(total)
        
        total = total.lstrip('0') or '0'

        new_root = Node(int(total[0]))
        curr = new_root

        for i in range(1, len(total)):
            curr.next = Node(int(total[i]))
            curr = curr.next

        return new_root
        