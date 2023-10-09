# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        traversedNodes = set()
        
        current = head
        
        while current is not None:
            
            if hash(current) in traversedNodes:
                return True
            
            traversedNodes.add(hash(current))
            
            current = current.next
            
        return False
    
    
if __name__ == '__main__':
    
    l3 = ListNode(3)
    l2 = ListNode(2)
    l0 = ListNode(0)
    ln4 = ListNode(-4)
    l3.next = l2
    l2.next = l0
    l0.next = ln4
    ln4.next = l2
    
    s = Solution()
    s.hasCycle(l3)