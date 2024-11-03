class Solution:

    def isLengthEven(self, head):
        # Code here
        length = 0

        curr = head

        while curr:
            length += 1
            curr = curr.next

        return True if length % 2 == 0 else False