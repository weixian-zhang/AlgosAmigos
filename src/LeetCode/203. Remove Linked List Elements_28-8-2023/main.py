# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val: int):

        if head == None or head == []:
            return None


        if head.val == val:
            next = head.next
            head = next


        dummyHead = ListNode(next=head)
        current = head
        prev = dummyHead


        while current != None:

            next = current.next

            if current.val == val:
                prev.next = next
            else:
                prev = current

            current = next


        return dummyHead.next


if __name__ == '__main__':

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(6)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next  = ListNode(4)
    # head.next.next.next.next.next  = ListNode(5)
    # head.next.next.next.next.next.next = ListNode(6)

    head = ListNode(7)
    head.next = ListNode(7)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(7)

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)

    s = Solution()
    s.removeElements(head, 7)

