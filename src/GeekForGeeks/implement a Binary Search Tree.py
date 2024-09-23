class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BinarySeachTree:
    
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, num: int):
        if not self.root:
            self.root = Node(num)
            return
        
        def _insert(node: Node):
            if not node:
                return Node(num)
            
            if num > node.val:
                node.right = _insert(node.right)
            else:
                node.left = _insert(node.left)

            return node

        _insert(self.root)

    def delete_with_return(self, num: int):
        
        def _delete(node: Node, num):
            if not node:
                return node
            
            if num > node.val:
                node.right = _delete(node.right, num)
            elif num < node.val:
                node.left = _delete(node.left, num)
            else:

                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                minOnRight = node.right
                while minOnRight.right:
                    minOnRight = minOnRight.right

                node.val = minOnRight.val
                node.right = _delete(node.right, num)

            return node

        _delete(self.root, num)

    def delete_without_return(self, num: int):
        
        def _delete(parent: Node, node: Node, num):

            if not node:
                return

            if num > node.val:
                _delete(node, node.right, num)
            elif num < node.val:
                _delete(node, node.left, num)
            else:
                # leaf node
                if not node.left:
                    if parent:
                        if parent.left == node:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    else:
                        self.root = None
                elif not node.right:
                    if parent:
                        if parent.left == node:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    else:
                        self.root = None

                # both left and right node exist
                else:
                    # find max on left
                    minOnRight = node.right
                    while minOnRight.left:
                        minOnRight = minOnRight.left

                    node.val = minOnRight.val
                    _delete(node, node.right, minOnRight.val)

                    

        _delete(self.root, self.root, num)

    def find(self, num: int):
        pass



bst = BinarySeachTree()
bst.insert(7)
bst.insert(5)
bst.insert(20)
bst.insert(4)
bst.insert(18)
bst.insert(25)
bst.insert(2)
bst.insert(11)
bst.insert(19)
bst.insert(33)
bst.insert(1)
bst.insert(3)
bst.insert(14)
bst.insert(28)
bst.insert(12)
bst.insert(10)
bst.insert(13)
bst.insert(17)
bst.insert(15)
bst.insert(31)

# bst.delete(11)
# bst.delete(33)
bst.delete_without_return(14)

