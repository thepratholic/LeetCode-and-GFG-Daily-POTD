# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def getDecimalValue(self, head) -> int:
        ans = 0
        res = []
        temp = head

        while temp != None:
            res.append(temp.val)
            temp = temp.next

        res.reverse()

        for i in range(len(res)):
            if res[i] == 1:
                ans += (2 ** i)

        return ans        