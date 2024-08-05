
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    # my solution - breadth first search
    # space (n)
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root
        
        queue, childrenNodes = [], []

        queue.append(root)

        while queue:

            currParents = []
            while queue:

                n = queue.pop(0)

                currParents.append(n)

                if n.left: childrenNodes.append(n.left)
                if n.right: childrenNodes.append(n.right)

            # link next node to right node
            if len(currParents) > 1:
                i = len(currParents) - 1
                j = i - 1
                while j >= 0:
                    currParents[j].next = currParents[i]
                    j -=1
                    i -= 1

            # add children nodes to queue and continue the algorithm
            while childrenNodes:
                queue.append(childrenNodes.pop(0))
               
        return root
    
    # most votes solution
    # space O(1)
    def connect(self, root: 'Node') -> 'Node':

        head, prev = None, None
        cur = root

        while cur:
            
            while cur:  # iterate on the current level

                # left child
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    
                    prev = cur.left
                
                # right child
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    
                    prev = cur.right
                
                # move to next node
                cur = cur.next
            
            # move to next level
            cur = head
            head = None
            prev = None
        
        return root

    


n3 = Node(3, Node(7))
n2 = Node(2, Node(4), Node(5))
n1 = Node(1, n2, n3)

s = Solution()
s.connect(n1)
