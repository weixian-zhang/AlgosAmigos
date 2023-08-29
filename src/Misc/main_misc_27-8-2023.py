
# Linked List
class Node:
    def __init__(self, data = 0) -> None:
        self.data = data
        self.next = None
class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def add(self, data) -> None:
        
        if self.head == None:
            self.head = Node(data)
            return
            
        current = self.head
        
        while current != None:
            next = current.next
            
            if next == None:
                current.next = Node(data)
                return
                
            current = next
            
    
    def get(self, index):
        
        if index == 0:
            return self.head.data
        
        current_idx = 0
        
        def _get(node, index, current_idx):
            
            if current_idx == index:
                return node.data
            
            if node.next == None:
                return -1
            
            current_idx += 1
            
            return _get(node.next, index, current_idx)
            
        
        return _get(self.head, index, 0)
            
            
    
    def find(self, data) -> bool:
        
        if self.head == None:
            return False
        if self.head.data == data:
            return True
        
        current = self.head
        
        while current != None:
            
            next = current.next
            
            if current.data == data:
                return True
            
            current = next
        
        return False
    
    def delete(self, data) -> None:
        
        if self.head == None:
            return
        
        if self.head.data == data:
            next = self.head.next
            self.head = next
            return
        
        dummyHead = Node(-1)
        dummyHead.next = self.head
        
        prev = dummyHead
        current = self.head
        
        while current != None:
            
            next = current.next
            
            if current.data == data:
                prev.next = current.next
            else:
                prev = current
                
            current = next
        

    def display(self):
        
        if self.head == None:
            return 'no nodes'
        
        result = []
        current = self.head
        
        while current != None:
            
            next = current.next
            result.append(current.data)

            current = next
            
        return ' -> '.join([str(x) for x in result])
        
    def reverse(self) -> Node:
        
        prev = None
        current = self.head
        
        while current != None:
            
            next = current.next
            
            current.next = prev
            
            prev = current
            
            current = next
        
        self.head = prev
        


# DFS graph traversal
class DFS:
    
    def __init__(self) -> None:
        
        graph = {
            0, [()]
        }

class BFS:
    pass



# Dijkstra shortest path

# tree traversal
    # pre, in, post order
    
# binary search tree
class BSTNode:
    def __init__(self , value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def has_one_child(self):
        if self.left is not None or self.right is not None:
            return True
        return False
    
    def has_both_child(self):
        if self.left is not None and self.right is not None:
            return True
        return False
    
class BinarySearchTree:
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        
        if self.root == None:
            self.root = BSTNode(value)
            return
        
        def _traverse(node):
            nonlocal value

            if node == None:
                node = BSTNode(value)
            
            if value < node.value:
                 node.left = _traverse(node.left)
                 print(node.left)
            elif value > node.value:
                 node.right = _traverse(node.right)
                 #print(node.right.value)
                 
            return node
                 
        _traverse(self.root)
        
    
    def update(self, value):
        pass
    
    def delete(self, value):
    
        # node_to_del = self.find_by_value(value)
        # print(f'node to delete: {node_to_del.value}')
        
        def _recurse(node: BSTNode):
            
            nonlocal value
            
            if node is None:
                return None
            
            if value < node.value:
                node.left = _recurse(node.left)

            elif value > node.value:
                node.right = _recurse(node.right)
            
            # node found, value == node.value
            else:
                
                 if node.left is None and node.right is None:
                     node = None
            
                # one child, either left or right, successor take over
                 elif node.has_one_child():
                     pass
                 
                 # # both left and right children
                    # get either largest value of left node or smallest value of right node
                    # update node-to-del value with replace largest or smallest
                    # delete largest or smallest node by recursively going through same process
                 else:
                     pass
            
            return node
        
            # # leaf node, no child
            # if node_to_del.left is None and node_to_del.right is None:
            #     node_to_del = None
            
            # # one child, either left or right, successor take over
            # elif node_to_del.has_one_child():
            #     if node_to_del.left is not None:
            #         successor = node_to_del.left
            #     else:
            #         successor = node_to_del.right
                
            #     node_to_del = successor
            
            # # both left and right children
            #     # get either largest value of left node or smallest value of right node
            #     # update node-to-del value with replace largest or smallest
            #     # delete largest or smallest node by recursively going through same process
            # else:
            #     largest_node_on_left = self.find_max_value(node_to_del.left)
                
            #     node_to_del = largest_node_on_left
                
            #     # now to delete largest node on left
            #     _recurse(largest_node_on_left.value)
                
                
        _recurse(self.root)
        
            
        
    
    # same as DFS
    def pre_order_traversal(self) -> str:
        
        result = []
        
        def _recurse(node):
            
            if node == None: return
            
            result.append(node.value)
            
            _recurse(node.left)
            _recurse(node.right)
        
        _recurse(self.root) 
        
        return ' -> '.join([str(x) for x in result])
        
    
    def in_order_traversal(self):
        
        result = []
        
        def _recurse(node):
            
            if node == None:
                return
            
            _recurse(node.left)
            
            result.append(node.value)
            
            _recurse(node.right)
            
        _recurse(self.root)
        
        return ' -> '.join([str(x) for x in result])
            
    
    def post_order_traversal(self):
        
        result = []
        
        def _recurse(node):
            
            if node == None:
                return 
            
            _recurse(node.left)
            
            _recurse(node.right)

            result.append(node.value)
            
        _recurse(self.root)
        
        return ' -> '.join([str(x) for x in result])
            
    
    from queue import PriorityQueue
    # breadth first search
    def level_order_traversal(self) -> str:
        
        if self.root is None:
            return ''
        
        result = []
        queue = []
        
        queue.append(self.root)
        
        
        while len(queue) > 0:
            
            node = queue.pop(0)
            
            result.append(node.value)
            
            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
                
        
        return ' -> '.join([str(x) for x in result])
        
        
    
    # depth of tree from root to last level leaf node
    def height(self):
        pass
    
    #https://www.youtube.com/watch?v=fAAZixBzIAI&t=1422s
    def sum(self): 
        pass
    
    def find_by_value(self, value) -> BSTNode:
        
        if self.root == None:
            return None
        
        def _find(node):
            
            nonlocal value
            
            if node == None: return None
            
            if value < node.value:
                node = _find(node.left)
                
            elif value > node.value:
                node = _find(node.right)
            
            
            return node
        
        node = _find(self.root)
        
        return node
    
    def find_min_value(self, node) -> BSTNode:
        pass
    
    def find_max_value(self, node) -> BSTNode:
        pass

# https://www.youtube.com/watch?v=us0cYQXQpxg
# permutations - of string with no repetition to get unique codes

class Permutation:
    
    def permute(self, strInput = 'abcde'):
        
        if not strInput:
            return []
        
        strings = [x for x in strInput]
        
        def _recurse(strings):
            
            if len(strings) == 0:
                return [[]]
            
            temp_perms = []
            
            first_char = strings[0]
            
            perms_without_first_char = _recurse(strings[1:])
            
            for permArr in perms_without_first_char:
                
                if len(permArr) == 0:
                    temp_perms.append([first_char])
                    break
                
                for idx in range(len(permArr)):
                    
                    first_part = permArr[0:idx]
                    
                    second_part = permArr[idx:]
                    
                    temp = first_part + [first_char] + second_part
                    
                    temp_perms.append(temp)
                
                first_char_at_back = permArr + [first_char]
                
                temp_perms.append(first_char_at_back)
                    
            return temp_perms
          
                    
        perms = _recurse(strings)         
            
        return perms


# https://www.youtube.com/watch?v=NA2Oj9xqaZQ
# combination - of string with no repetition to get unique codes

class Combinations:
    
    def gen_combo(self, strInput = 'abcd'):
        
        if not strInput:
            return [[]]
        
        result = []
        strings = [x for x in strInput]
        
        def _combos(strings):
            
            if len(strings) == 0:
                return [[]]
            
            first_char = strings[0]
            
            rest_of_chars = strings[1:]
            
            combos_without_first_char = _combos(rest_of_chars)
            
            combos_with_first_char = []
            
            for comboArr in combos_without_first_char:
                temp = comboArr + [first_char]
                combos_with_first_char.append(temp)
                
            return combos_without_first_char + combos_with_first_char
        
        combos = _combos(strings)
        return [x for x in combos if  len(x) > 0]

# merge sort
# https://www.youtube.com/watch?v=4VqmGXwpLqc
# https://www.youtube.com/watch?v=KF2j-9iSf4Q
# https://www.youtube.com/watch?v=cVZMah9kEjI
import math
class MergeSorter:
    
    def merge_sort(self, nums):
        
        if len(nums) == 1:
            return nums
        
        middle_index = int(len(nums) / 2)
        
        leftArr = self.merge_sort(nums[:middle_index])
        
        rightArr = self.merge_sort(nums[middle_index:])
        
        merged = self._merge(leftArr, rightArr)
        
        return merged
    
    def _merge(self, leftArr, rightArr):
        
        merged = []
        i = 0
        j = 0
        while i < len(leftArr) and j < len(rightArr):
            
            if leftArr[i] < rightArr[j]:
                merged.append(leftArr[i])
                i += 1
            else:
                merged.append(rightArr[j])
                j += 1
            

        
        # there are elements in either one of left or right array
        # remember adds these "leftovers"
        
        while i < len(leftArr):
            merged.append(leftArr[i])
            i += 1
            
        while j < len(rightArr):
            merged.append(rightArr[j])
            j += 1
            
        return merged





# quick sort




if __name__ == '__main__':
    
    # permutation = Permutation()
    # r = permutation.permute()
    # print(len(r))
    # print(r)
    
    # combination = Combinations()
    # combos = combination.gen_combo()
    # print(len(combos))
    # print(combos)
    
    # ms = MergeSorter()
    # sorted = ms.merge_sort([2,6,5,1,7,4,3])
    # print(sorted)
    
    # linked list
    # ll = LinkedList()
    # ll.add(1)
    # ll.add(2)
    # ll.add(3)
    # ll.add(4)
    # ll.add(5)
    # print(ll.display())
    
    # ll.reverse()
    # print(ll.display())
    
    # ll.reverse()
    # print(ll.display())
    
    # print(ll.get(-6))
    # print(ll.find(4))
    
    # ll.delete(3)
    # print(ll.display())
    
    # ll.delete(1)
    # print(ll.display())
    
    # ll.delete(4)
    # print(ll.display())
    
    # ll.delete(5)
    # print(ll.display())
    
    # ll.delete(2)
    # print(ll.display())
    
    # ll.add(2)
    # print(ll.display())
    
    
    # binary search tree
    bst = BinarySearchTree()
    
    bst.insert(10)
    bst.insert(6)
    bst.insert(21)
    bst.insert(5)
    bst.insert(8)
    bst.insert(18)
    # bst.insert(30)
    # bst.insert(15)
    # bst.insert(25)
    # bst.insert(1)
    # bst.insert(40)
    # bst.insert(20)
    
    # print('pre order')
    # print(bst.pre_order_traversal())
    
    # print('in order')
    # print(bst.in_order_traversal())
    
    # print('post order')
    # print(bst.post_order_traversal())
    
    # print('level order')
    # print(bst.level_order_traversal())
    
    bst.delete(18)
    print(bst.level_order_traversal())
    
    
    
    