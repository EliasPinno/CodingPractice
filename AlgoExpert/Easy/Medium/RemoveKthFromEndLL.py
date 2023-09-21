# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    front = head
    back = head
    runningLen = 0
    for i in range(k+1):
        if front == None:
            head.value = head.next.value
            head.next = head.next.next
            return head
        front = front.next
    while front != None:
        front = front.next
        back = back.next
    back.next = back.next.next
    return head
# O(n) time, O(1) space