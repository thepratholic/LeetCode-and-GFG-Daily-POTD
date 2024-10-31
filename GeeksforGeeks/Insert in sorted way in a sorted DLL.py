#User function Template for python3
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def sortedInsert(self, head, x):
    #code here
        tmp = Node(x)
        if head is None:
            return tmp

        if x < head.data:
            tmp.next = head
            head.prev = tmp
            return tmp

        curr = head
        while curr.next and curr.next.data < x:
            curr = curr.next

        tmp.next = curr.next
        tmp.prev = curr

        if curr.next:
            curr.next.prev = tmp

        curr.next = tmp
        return head