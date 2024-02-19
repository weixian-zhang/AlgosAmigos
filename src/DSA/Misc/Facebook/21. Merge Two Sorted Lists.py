
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 43 ms, faster than 31.19% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 16.7 MB, less than 54.81% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()

        currDummy, curr1, curr2 = dummy, list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                currDummy.next = ListNode(curr1.val)
                currDummy = currDummy.next
                curr1 = curr1.next

            elif curr1.val > curr2.val:
                currDummy.next = ListNode(curr2.val)
                currDummy = currDummy.next
                curr2 = curr2.next

            else:
                currDummy.next = ListNode(curr1.val)
                currDummy = currDummy.next
                curr1 = curr1.next

                currDummy.next = ListNode(curr2.val)
                currDummy = currDummy.next
                curr2 = curr2.next

        while curr1:
            currDummy.next = ListNode(curr1.val)
            currDummy = currDummy.next
            curr1 = curr1.next

        while curr2:
            currDummy.next = ListNode(curr2.val)
            currDummy = currDummy.next
            curr2 = curr2.next

        return dummy.next
                

# l1 = ListNode(1, next=ListNode(2, next=ListNode(3)))
# l2 = ListNode(1, next=ListNode(3, next=ListNode(4)))
l1 = ListNode(5)
l2 = ListNode(1, next=ListNode(2, next=ListNode(4)))

s = Solution()
s.mergeTwoLists(l1, l2)