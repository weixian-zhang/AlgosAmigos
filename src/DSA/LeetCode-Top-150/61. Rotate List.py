# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head 
        
        nodeCount = self._get_node_count(head)

        if k > nodeCount:
            k = k % nodeCount
        
        # rotate K times
        for _ in range(k):

            curr = head
            prev = curr

            # prev = 2nd last node, curr = last node
            while curr and curr.next:
                prev = curr
                curr = curr.next
            
            curr.next = head
            prev.next = None
            head = curr

        return head
    
    def _get_node_count(self, head: ListNode):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

        

s = Solution()

# l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# s.rotateRight(l1, 2)

l1 = ListNode(0, ListNode(1, ListNode(2)))
s.rotateRight(l1, 4)
