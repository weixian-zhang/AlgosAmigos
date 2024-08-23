from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            e.g: linkedlist 1, 2, 3
            prev stores the state of curr, at the point when curr cuts of next-link to next
        '''

        prev, curr = None, head

        while curr:
            
            next = curr.next

            curr.next = prev

            prev = curr
            
            curr = next

        return prev 
    
ln = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()

r = s.reverseList(ln)

pass

