from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def _reverse(startNode: ListNode, endNode: ListNode):
            
            dummy = ListNode(-1)
            prev = dummy
            curr = startNode
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            rHead, rTail = prev, prev


            while rTail.next.val != -1:
                    rTail = rTail.next

            rTail.next = None

            return rHead, rTail   # which is startNode
        
        isFirstRotate = True
        startRev = None
        curr, lastRotatedTail = head, None

        newK = k - 1

        while curr:

            if newK > 0:
                if not startRev:
                    startRev = curr
                curr = curr.next
                newK -= 1
            
            else:
                
                next = curr.next

                curr.next = None

                if not startRev:
                    startRev = curr

                rHead, rTail = _reverse(startRev, curr)

                if isFirstRotate:
                    head = rHead
                    isFirstRotate = False
                    lastRotatedTail = rTail
                    lastRotatedTail.next = next
                else:
                    lastRotatedTail.next = rHead
                    lastRotatedTail = rTail 

                curr = next

                startRev = None

                newK = k - 1

        if startRev:
            lastRotatedTail.next = startRev


        return head





l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6) )))))

s = Solution()
# s.reverseKGroup(l1, 2)
# s.reverseKGroup(l1, 3)
# s.reverseKGroup(l1, 2)
s.reverseKGroup(l1, 1)