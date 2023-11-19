# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        lnLen = 0
        curr = head

        # find length
        while curr:
            lnLen += 1
            curr = curr.next
        
        if lnLen == 1 and n == 1:
            return None
        

        curr = head
        prev = curr
        nodeCount = 1
        nodeToDel = (lnLen + 1) - n

        while curr:

            if nodeCount == nodeToDel:
                if prev == curr:
                    return curr.next
                else:
                    prev.next = curr.next
                    return head

            prev = curr
            curr = curr.next
            nodeCount += 1

        return head




l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#l1 = ListNode(1, ListNode(2))
#l1 = ListNode(1, ListNode(2, ListNode(3)))
s = Solution()
s.removeNthFromEnd(l1, 2)