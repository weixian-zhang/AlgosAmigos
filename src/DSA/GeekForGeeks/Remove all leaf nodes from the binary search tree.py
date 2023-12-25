# Given a binary tree, the value of node is distinct. 
# we can remove the leaf node each time until there is no node in the tree. 
# We put the remove node into a list, and be sorted and put the sorted list to the anwer list. 
# Bottom-up is required. Output is List>


# Create a newNode in binary search tree. 
class TreeNode: 

    # Constructor to create a new node 
    def __init__(self, data: int): 
        self.data: int = data 
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    # insert with return
    # def insert(self, data: int):
    #     if not self.root:
    #         self.root = TreeNode(data)
    #         return
        
    #     def _insert(node: TreeNode, data: int):
             
    #          if not node:
    #              return TreeNode(data)
            
    #          if data < node.data:
    #              node.left = _insert(node.left, data)

    #          if data > node.data:
    #              node.right = _insert(node.right, data)
    
    # insert without 
    def insert(self, data: int):
        if not self.root:
            self.root = TreeNode(data)
            return
        
        def _insert(node: TreeNode, data: int):
            
             if data < node.data:
                 if not node.left:
                    node.left = TreeNode(data)
                 else:
                    _insert(node.left, data)

             if data > node.data:
                 if not node.right:
                    node.right = TreeNode(data)
                 else:
                    _insert(node.right, data)
        

        _insert(self.root, data)

    def print(self):

        def _traverse(node: TreeNode):
            if not node:
                return
            
            _traverse(node.left)

            print(node.data)

            _traverse(node.right)

        _traverse(self.root)

    # with return
    def delete_leaf_nodes_with_return(self):
        
        def _delete(node: TreeNode, deletedNodes: list[int]):
            
            if not node:
                return node
            
            node.left = _delete(node.left, deletedNodes)

            node.right = _delete(node.right, deletedNodes)

            if not node.left and not node.right:
                deletedNodes.append(node.data)
                return None

            return node
        
        deletedNodes = []

        while self.root:
            self.root = _delete(self.root, deletedNodes)
        return deletedNodes
    
    def delete_leaf_nodes_WithOut_return(self):

        def _delete(parent: TreeNode,current: TreeNode, deletedNodes: list[int]):
            if not current:
                return
            
            if current.left:
                _delete(current, current.left, deletedNodes)
            elif current.right:
                _delete(current, current.right, deletedNodes)
            else:
                # is leaf node
                if not current.left and not current.right:
                    deletedNodes.append(current.data)
                    if not parent.left and not parent.right:
                        self.root = None
                    elif parent.left:
                        parent.left = None
                    else:
                        parent.right = None

        deletedNodes = []
        
        while self.root:
            _delete(self.root, self.root, deletedNodes)

        return deletedNodes


bst = BinarySearchTree()
bst.insert(49)
bst.insert(38)
bst.insert(59)
bst.insert(25)
bst.insert(20)
bst.insert(9)
bst.insert(7)

bst.print()

print(bst.delete_leaf_nodes_with_return())
# print(bst.delete_leaf_nodes_WithOut_return())
