class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newNode = ListNode(-1)
        newCurr = newNode
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:

            if curr1.val <= curr2.val:
                newCurr.next = ListNode(curr1.val)
                newCurr = newCurr.next
                curr1 = curr1.next
 
            else:
                newCurr.next = ListNode(curr2.val)
                newCurr = newCurr.next
                curr2 = curr2.next
        
        while curr1:
            newCurr.next = ListNode(curr1.val)
            newCurr = newCurr.next
            curr1 = curr1.next

        while curr2:
            newCurr.next = ListNode(curr2.val)
            newCurr = newCurr.next
            curr2 = curr2.next

        return newNode.next