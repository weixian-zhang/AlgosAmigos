# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Woot!
# Runtime: 34 ms, faster than 92.40% of Python3 online submissions for Partition List.
# Memory Usage: 16.4 MB, less than 22.66% of Python3 online submissions for Partition List.
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return head
        
        nodesLesserX = []
        # look for nodes lesser than x, detach them and put in list
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            if curr.val < x:

                nodesLesserX.append(curr)

                # on first node
                if prev == dummy:
                    dummy.next = curr.next
                    curr = dummy.next
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next

        #loop nodesLesserX right to left to preserve position
        # attach node back to linked list
        for x in range(len(nodesLesserX)-1, -1, -1):

            n = nodesLesserX[x]
            next = dummy.next
            n.next = next
            dummy.next = n

        return dummy.next



l1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
s = Solution()
s.partition(l1, 3)