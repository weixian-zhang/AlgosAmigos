from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution:

    # hashset store visited
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()

        curr = head

        while curr and curr.next:
            
            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next

        return False

    # Floyd's cycle finding or Hare/Tortoise  slow/fast pointer
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        slow, fast = head, head

        while slow and fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    

s = Solution()

# 1 -> 2 -> 3 ->4 -> 5 -> 6 -> 1
# n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
# n6 = n1.next.next.next.next.next
# n6.next = n1

# 1 -> 2 -> 3 ->4 -> 2
n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
n4 = n1.next.next.next
n2 = n1.next
n4.next = n2

s.hasCycle(n1)
