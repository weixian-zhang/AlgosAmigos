from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # iterative with 2 pointers, prev and curr
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
    
    # recursive
    # head recursion to go last node, from last node, set next pointer to previous
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
                
        # head recursion to go last node
        new_head = self.reverseList(head.next)

        front = head.next

        front.next = head 

        head.next = None
            
        return new_head

    
# ln = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ln = ListNode(1, ListNode(2, ListNode(3)))

s = Solution()
r = s.reverseList(ln)

def create_ll_from_list(nums: list[int]):

    dummy = ListNode(-1)
    curr = dummy

    for n in nums:
        new_node = ListNode(n)
        curr.next = new_node
        curr = curr.next

    return dummy.next


new_ln = create_ll_from_list([1,2,3,4,5])

pass


