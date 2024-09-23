from typing import List, Optional

import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nums = []
        dummy = ListNode()
        resultCurr = dummy

        for ll in lists:
            curr = ll
            while curr:
                heapq.heappush(nums, curr.val)
                curr = curr.next
        
        while nums:
            n = heapq.heappop(nums)
            resultCurr.next = ListNode(n)
            resultCurr = resultCurr.next

        return dummy.next
    

s = Solution()

ll1 = ListNode(1, ListNode(4, ListNode(5)))
ll2 = ListNode(1, ListNode(3, ListNode(4)))
ll3 = ListNode(2, ListNode(6))

s.mergeKLists([ll1,ll2, ll3])