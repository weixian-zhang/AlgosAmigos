
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
import copy
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        
        dummy = Node(-1)
        curr_dummy = dummy

        oldToCopyTracker = { None: None }

        curr = head

        while curr:
            
            cNode = Node(curr.val)

            oldToCopyTracker[curr] = cNode
            
            curr = curr.next  

        curr = head

        while curr:
            
            nextNode = oldToCopyTracker[curr.next]
            randNode = oldToCopyTracker[curr.random]

            currCopyNode = oldToCopyTracker[curr]
            currCopyNode.next = nextNode
            currCopyNode.random = randNode

            curr = curr.next

        return oldToCopyTracker[head]

                
                

            

            
            
    


#[[3,null],[3,0],[3,null]]


l1= Node(1, None, Node(7))
l10 = Node(10, l1, Node(11))
l11 = Node(11, l10, Node(1))
l13 = Node(13, l11, Node(7))
l7 = Node(7, l13, None)

l13.random = l7
l11.random = l1
l10.random = l11
l1.random = l7


s = Solution()
s.copyRandomList(l7)