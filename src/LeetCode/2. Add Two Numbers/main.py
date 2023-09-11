# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        rlsDummy = ListNode(-1)
        currentDummy = rlsDummy
        
        current1 = l1
        
        current2 = l2
        
        carryForward = 0
        
        # iterate both linkedlist together
        while current1 is not None and current2 is not None:
            
            next1 = current1.next
            next2 = current2.next
            
            currentVal = 0
            sumOfNodes = current1.val + current2.val + carryForward
            
            currentVal = sumOfNodes
            
            if sumOfNodes >= 10:
                
                carryForward = sumOfNodes // 10  # get "left side" of number
                currentVal = sumOfNodes % 10    # get "right side" of sum, which is divide by 10 get the remainder
            
            else:
                currentVal = sumOfNodes
                carryForward = 0    # reset carryForward            
            
            currentDummy.next = ListNode(currentVal)
            currentDummy = currentDummy.next
            
            current1 = next1
            current2 = next2
                
        
        # one of the LinkedList is at the "end", which means next is None
        if current1 is not None:
            
            while current1 is not None:
            
                next = current1.next
                
                sumOfNodes = current1.val + carryForward
                currentVal = sumOfNodes

                if sumOfNodes >= 10:
                    carryForward = sumOfNodes // 10
                    currentVal = sumOfNodes % 10
                else:
                    carryForward = 0
                    
                currentDummy.next = ListNode(currentVal)
                currentDummy = currentDummy.next
                
                current1 = next
                
                
        if current2 is not None:
            
            while current2 is not None:
            
                next = current2.next
                
                sumOfNodes = current2.val + carryForward
                currentVal = sumOfNodes

                if sumOfNodes >= 10:
                    carryForward = sumOfNodes // 10
                    currentVal = sumOfNodes % 10
                else:
                    carryForward = 0
                    
                currentDummy.next = ListNode(currentVal)
                currentDummy = currentDummy.next
                
                current2 = next
            
        # all nodes summed, left with carryForward
        if carryForward > 0:
            
            currentDummy.next = ListNode(carryForward)
            currentDummy = currentDummy.next
        
        
        return rlsDummy.next
    
            


if __name__ == '__main__':
    
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(1)
    
    l2 = ListNode(1)
    
    # l1 = ListNode(9)
    # l1.next = ListNode(9)
    # l1.next.next = ListNode(9)
    # l1.next.next.next = ListNode(9)
    # l1.next.next.next.next = ListNode(9)
    # l1.next.next.next.next.next = ListNode(9)
    # l1.next.next.next.next.next.next = ListNode(9)
    
    # l2 = ListNode(9)
    # l2.next = ListNode(9)
    # l2.next.next = ListNode(9)
    # l2.next.next.next = ListNode(9)
    
    s = Solution()
    s.addTwoNumbers(l1, l2)