class Solution:
    def reverseList(self, head):
        # Code here
        
        prev = None
        temp = head
        if temp is None:
            return None
            
        if temp.next is None:
            return head
            
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            
        return prev
