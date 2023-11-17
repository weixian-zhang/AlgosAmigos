# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 54 ms, faster than 95.63% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 16.6 MB, less than 6.69% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(-1)
        dummyPointer = dummy
        carry = 0
        l1Next = l1
        l2Next = l2

        while l1Next is not None and l2Next is not None:

            result = l1Next.val + l2Next.val + carry
            carry = 0

            if result >= 10:
                carry = result // 10
                remain = result % 10
                dummyPointer.next = ListNode(remain)
            else:
                dummyPointer.next = ListNode(result)
            
            dummyPointer = dummyPointer.next
            l1Next = l1Next.next
            l2Next = l2Next.next

        while l1Next is not None:

            result = l1Next.val + carry
            carry = 0

            if result >= 10:
                carry = result // 10
                remain = result % 10
                dummyPointer.next = ListNode(remain)
            else:
                dummyPointer.next = ListNode(result)

            dummyPointer = dummyPointer.next
            l1Next = l1Next.next

        
        while l2Next is not None:

            result = l2Next.val + carry
            carry = 0

            if result >= 10:
                carry = result // 10
                remain = result % 10
                dummyPointer.next = ListNode(remain)
            else:
                dummyPointer.next = ListNode(result)

            dummyPointer = dummyPointer.next
            l2Next = l2Next.next

        
        if carry != 0:
            dummyPointer.next = ListNode(carry)
            carry = 0

        return dummy.next
    

    def _ll_to_list(self, node: ListNode):
        
        r = []
        pointer = node

        while pointer is not None:
            r.append(pointer.val)
            pointer = pointer.next

        return r








l1 = ListNode(9, ListNode(9, ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9,ListNode(9))))

s = Solution()
r = s.addTwoNumbers(l1, l2)
print(s._ll_to_list(r))