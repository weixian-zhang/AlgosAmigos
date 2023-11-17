
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        
        dummy = Node(-1)
        dummyPointer = dummy
        nodeIndexer = {}
        curr = head

        while curr:

            if curr.next:
                dummyPointer.next = Node(x=curr.val, next=Node(curr.next.val), random=curr.random)
            else:
                dummyPointer.next = Node(x=curr.val, next = None, random=curr.random)

            nodeIndexer[hash(dummyPointer.next)] = dummyPointer.next

            dummyPointer = dummyPointer.next
            curr = curr.next

        curr = dummy.next

        while curr:

            if curr.random:
                randomNode = nodeIndexer[hash(curr.random)]
                curr.random = randomNode
            else:
                curr.random = None

            curr = curr.next

        return dummy.next


#[[3,null],[3,0],[3,null]]


l1= Node(1, None, Node(7))
l10 = Node(10, l1, Node(11))
l11 = Node(11, l10, Node(1))
l13 = Node(13, l11, Node(7))
l7 = Node(7, l13, None)


s = Solution()
s.copyRandomList(l7)