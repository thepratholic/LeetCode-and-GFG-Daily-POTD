"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        curr = head
        cnt = 0
        while curr is not None:
            if curr.data == key:
                cnt += 1

            curr = curr.next

        return cnt