# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        current = head
        prev = None
        next = None
    
        
        while current is not None:
            
            next = current.next
            
            current.next = prev
            
            prev = current
                
            current = next
            
        return prev
    
    
    
if __name__ == '__main__':
    
    s = Solution()
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    
    s.reverseList(l1)