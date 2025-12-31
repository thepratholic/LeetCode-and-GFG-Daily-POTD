'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        
        temp = head
        
        ans = []
        
        while temp:
            ans.append(temp.data)
            temp = temp.next
            
        
        if ans == ans[::-1]:
            return True
            
        else:
            return False