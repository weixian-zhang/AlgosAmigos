

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None
        
        
n8 = Node(8)
n3 = Node(3)
n10 = Node(10)
n1 = Node(1)
n6 = Node(6)
n14 = Node(14)
n4 = Node(4)
n7 = Node(7)
n13 = Node(13)

n8.left = n3
n8.right = n10
n3.left = n1
n3.right = n6
n10.right = n14
n6.left = n4
n6.right = n7
n14.left = n13





class BinarySearchTree:
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val) -> None:
        
        if self.root == None:
            self.root = Node(val)
            return
        
        if self.root == val:
            self._insert(self.root.right, val)
            
        self._insert(self.root, val)
        
        
    def _insert(self, node, val):
        
        if node == None:
            return Node(val)
        
        if val > node.value:
            if node.right == None:
                node.right = Node(val)
                return
            else:
                return self._insert(node.right, val)
        
        if node.left == None:
            node.left = Node(val)
        else:
            return self._insert(node.left, val)
            

    def search(self, target)-> Node:
        
        if self.root == None or self.root.value == target:
            return self.root
        
        return self._search(self.root, target)
    
    def _search(self, node, target):
        
        if self.root == None or self.root.value == target:
            return self.root
        
        if node == None:
            return None
        
        if node.value == target:
            return node
        
        if target > node.value:
            return self._search(node.right, target)
        
        return self._search(node.left, target)
    
    def get_level(self):
        
        def _level(node, level):
            
            if node == None: return level
            
            left_level = _level(node.left, level + 1)
            right_level = _level(node.right, level + 1)
            
            return max(left_level, right_level)
        
        return _level(self.root, 0)
    
    def find_height(self, k):
        
        height = 0
        
        def _find_height(node, level):
            
            nonlocal height
            
            if node == None: return 0
            
            if node.value == k: return level
            
            down_level = _find_height(node.left, level + 1)
            
            if down_level != 0:
                return down_level
                
            
            down_level = _find_height(node.right, level + 1)
            
            return down_level
        
            
        return _find_height(self.root, 1)
    
    def delete_node(self, node: Node, target_value):
    
        if node == None:
            return None
        
        #find node to delete
        if target_value > node.value:
            node.right = self.delete_node(node.right, target_value)
        elif target_value < node.value:
            node.left = self.delete_node(node.left, target_value)
            
        #found the node to delete
        elif node.value == target_value:
            
            node_to_del = node
                
            #case 1: no child
            if node_to_del.left == None and node_to_del.right == None:
                return None

            #case 2: 1 child either left or right
            elif node_to_del.left == None:
                return node_to_del.right
            elif node_to_del.right == None:
                return node_to_del.left
            
            #case 3: node with both left and right child
            else:
                
                # find min node value of right subtree
                current = node_to_del
                while current != None:
                    current = current.left
                min_val = current.left
                
                # use min val to set/replace node-to-del value
                node_to_del.value = min_val
                
                # recurse right subtree to delete the "duplicated" min value node
                self.delete_node(node_to_del.right, min_val)
        
        return node
            
            
                
                
                
        
            
    def print_pre_order(self):
        
        if self.root == None:
            print('tree is empty')
        
        def _print(curr_node):
            if curr_node != None:
                #node, left, right
                print(f'{curr_node.value}')
                _print(curr_node.left)
                _print(curr_node.right)
                
        _print(self.root)
    
    def print_in_order(self):
        
        if self.root == None:
            print('root is empty')
            
        def _print(node):
            
            if node != None:
                _print(node.left)
                print(node.value)
                _print(node.right)
                
        _print(self.root)
        

    
    def print_post_order(self):
        if self.root == None:
            print('tree is empty')
            return
        
        def _print(node):
            if node != None:
                _print(node.left)
                _print(node.right)
                print(node.value)
                
        _print(self.root)
    
                   



if __name__ == '__main__':
    
    bst = BinarySearchTree()
    
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(14)
    bst.insert(13)
    
    # print('pre order')
    # bst.print_pre_order()
    
    # print('in order')
    # bst.print_in_order()
    
    # print('post order')
    # bst.print_post_order()
    
    #print(bst.get_level())
    
    #print(bst.find_height(13))
    
    # node = bst.search(111)
    # val = node.value if node != None else 'None'
    # print(val)
    
    # searched_node = bst.search(8)
    # minNode = bst.find_min_on_left_subtree(searched_node)
    # print(minNode.value)
    
    