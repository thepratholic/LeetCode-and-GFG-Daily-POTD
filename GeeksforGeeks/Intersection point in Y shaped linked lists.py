def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersetPoint(headA,headB):

    if not headA or not headB:
        return -1

    lenA = get_length(headA)
    lenB = get_length(headB)

    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    while headA and headB:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next


    return -1