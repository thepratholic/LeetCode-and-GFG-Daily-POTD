from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st = set(nums)

        new_list_vals = []

        tmp = head

        while tmp:
            if tmp.val in st:
                tmp = tmp.next
            else:
                new_list_vals.append(tmp.val)
                tmp = tmp.next

        tmp = ListNode(new_list_vals[0])
        new_node = tmp

        for node in range(1, len(new_list_vals)):
            tmp.next = ListNode(new_list_vals[node])
            tmp = tmp.next

        return new_node