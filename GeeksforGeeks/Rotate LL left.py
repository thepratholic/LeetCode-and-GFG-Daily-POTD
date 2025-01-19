class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if head is None or k == 0:
            return head
        temp = head
        length = 1
        while temp.next is not None:
            length += 1
            temp = temp.next
            
        temp.next = head
        
        k %= length
        if k == 0:
            temp.next = None
            return head

        newTail = head
        for _ in range(k - 1):
            newTail = newTail.next
        
        # Step 4: Set the new head and break the connection
        newHead = newTail.next
        newTail.next = None
        
        # Step 5: Connect the old tail to the old head
        temp.next = head
        
        return newHead