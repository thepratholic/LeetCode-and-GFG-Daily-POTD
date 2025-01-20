
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self,list1, list2):
        # code here
        temp1 = list1
        temp2 = list2
        dummyNode = Node(-1)
        temp = dummyNode

        while temp1 is not None and temp2 is not None:
            if temp1.data < temp2.data:
                temp.next = temp1
                temp = temp1
                temp1 = temp1.next
            
            else:
                temp.next = temp2
                temp = temp2
                temp2 = temp2.next

        if temp1 is not None:
            temp.next = temp1
        else:
            temp.next = temp2

        return dummyNode.next