# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.currIdx = -1
        self.root = root

        self._bst_inorder_to_list()

        self.bstLen = len(self.nodes) - 1

    def next(self) -> int:
        self.currIdx += 1
        return self.nodes[self.currIdx].val

    def hasNext(self) -> bool:
        return self.currIdx + 1 <= self.bstLen

    def _bst_inorder_to_list(self) -> None:
        
        def recurse(node: TreeNode):
            
            if not node:
                return
            
            recurse(node.left)

            self.nodes.append(node)

            recurse(node.right)

        recurse(self.root)

n15 = TreeNode(15, TreeNode(9), TreeNode(20))
n7 = TreeNode(7, TreeNode(3), n15)

bSTIterator = BSTIterator(n7)
print(bSTIterator.next());    # return 3
print(bSTIterator.next());    # return 7
print(bSTIterator.hasNext()); # return True
print(bSTIterator.next());    # return 9
print(bSTIterator.hasNext()); # return True
print(bSTIterator.next());    # return 15
print(bSTIterator.hasNext()); # return True
print(bSTIterator.next());    # return 20
print(bSTIterator.hasNext()); # return False

# Your BSTIterator object will be instantiated and called as such:
