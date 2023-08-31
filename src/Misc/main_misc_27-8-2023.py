
class BinarySearch:
    
    def __init__(self) -> None:
        self.nums = [44, 22, 1,0,232,33,77,12,8,6,2]
        
        sorter = MergeSorter()
        
        self.nums = sorter.sort(self.nums)
        
    def search(self, target):
        low = 0
        high = len(self.nums) - 1
        
        
        while low <= high:
            
            middle = (high + low) // 2
            
            p_answer = self.nums[middle]
            
            if p_answer == target:
                return True, middle
            
            elif p_answer > target:
                high = middle - 1
            
            else:
                low = middle + 1
                
        return False, -1
    

# merge sort
# https://www.youtube.com/watch?v=4VqmGXwpLqc
# https://www.youtube.com/watch?v=KF2j-9iSf4Q
# https://www.youtube.com/watch?v=cVZMah9kEjI
class MergeSorter:
    
    def sort(self, nums):
        
        result = []
        
        def _recurse(nums):
            
            nonlocal result
            
            if len(nums) <= 1:
                return nums
            
            middle = len(nums) // 2
            
            leftArr = _recurse(nums[:middle])
            
            rightArr = _recurse(nums[middle:])
            
            result = self._merge(leftArr, rightArr)
            
            return result
        

        return _recurse(nums)
    
    def _merge(self, left, right) -> list[int]:
        
        result = []
        i = 0
        j = 0
        
        if left == [] or right == []:
            return left + right
        
        while i <= len(left)-1 and j <= len(right)-1:
            
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
                
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
                
            else:
                result.append(left[i])
                result.append(right[j])
                i += 1
                j += 1
        
        # merge remaining of left
        while i <= len(left)-1:
            result.append(left[i])
            i += 1
            
        
        #merge remaining of right
        while j <= len(right)-1:
            result.append(right[j])
            j += 1
        
        return result

# quick sort
                    
                    
class AdjacencyMatrix:
    
    def __init__(self) -> None:
        
        # nodes: a=0, b=1, c=2, d=3
        # adj_matrix = [
        #     [0,1,1,0],
        #     [1,0,0,1],
        #     [1,0,0,1],
        #     [0,1,1,0],
        # ]
        self.nodes = [0,1,2,3]
        self.adj_matrix = []
        for x in range(4):
            self.adj_matrix.append([0 for x in range(4)])
            
        self.add_edge(0,1)
        self.add_edge(0,2)
        self.add_edge(1,0)
        self.add_edge(1,3)
        self.add_edge(2,0)
        self.add_edge(2,3)
        self.add_edge(3,1)
        self.add_edge(3,2)
            
    def add_edge(self, src, dest):
        self.adj_matrix[src][dest] = 1
    
    
    def dfs(self, start):
        
        visited = []
        
        def _recurse(node):
            
            visited.append(node)
            
            # go thru column, i is the neighbour
            for i in range(len(self.nodes)):
                
                if self.adj_matrix[node][i] == 1 and i not in visited:
                        _recurse(i)
            
        start_node = 0
        
        _recurse(0)
        
        print(visited)


# algorithm pattern - sliding window
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def find_max_subarray(find_max_subarray_nums, k):
    
    largestSum = 0
    windows_size = k
    
    for i in range(len(find_max_subarray_nums) - windows_size):
        
        temp = sum(find_max_subarray_nums[i:i+windows_size])
        largestSum = max(temp, largestSum)
        
    print(largestSum)

# find smallest size/length of subarray where sub >= 8
def find_smallest_sub_array_size(find_max_subarray_nums, sumConstraint = 8):
    
    nums = smallest_sub_array_size_nums
    smallest_size_so_far = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            
            if sum(nums[i:j]) >= sumConstraint:
                
                current_size = j-i
                
                if smallest_size_so_far > 0:
                    smallest_size_so_far = min(current_size, smallest_size_so_far)
                        
                else:
                    smallest_size_so_far = current_size
                    
                break
            
    print(smallest_size_so_far)
      

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
        

import json
# DFS graph traversal
class DFS:
    
    def __init__(self) -> None:
        
        self.graph = {
            0: [1,2,3],
            1: [0],
            2: [3, 4],
            3: [0, 2],
            4: [ 2]
        }
        
    def search(self, startNode: int):
        
        visited = []
        
        def _recurse(node):
            
            visited.append(node)
            
            for n in self.graph[node]:
                
                if n not in visited:
                    _recurse(n)
        
        _recurse(0)
        
        print(','.join([str(x) for x in visited]))
        
            
            

class BFS:
    def __init__(self) -> None:
        
        self.graph = {
            0: [7,9,11],
            1: [8,10],
            2: [3,12],
            3: [2,4,7],
            4: [3],
            5: [6],
            6: [5,7],
            7: [0,3,6,11],
            8: [1,9,12],
            9: [0,8,10],
            10: [1,9],
            11: [0, 7],
            12: [2,8]
        }
        
    def traverse(self,node, end):
        
        visited = []
        queue = []
        parentTracker = {}
        levelTracker = {}
        
        queue.append(node)
        
        levelTracker[node] = 0
        
        while len(queue) > 0:
            
            current_node = queue.pop(0)
            
            if current_node not in visited:
                visited.append(current_node)
            
            for neighbour in self.graph[current_node]:
                
                if neighbour in visited:
                    continue
                
                
                
                # track each neighbour's parent 
                parentTracker[neighbour] = current_node
                
                # track number of hops from parent -> neightbour
                levelTracker[neighbour] = levelTracker[current_node] + 1
                
                queue.append(neighbour)
                
            
        path = self.backtrack_parent_to_get_path(parentTracker, end)
        distant = levelTracker[end]
        return ' -> '.join([str(x) for x in path]), distant
        
    
    # shortest number of node hops
    def backtrack_parent_to_get_path(self, parentTracker, destinationNode):
        
        node = parentTracker[destinationNode]
        
        result = []
        result.append(destinationNode)
        result.append(node)
        
        while node in parentTracker:
            node = parentTracker[node]
            result.append(node)
            
        result.reverse()
        return result



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
        if (self.left is None and self.right is not None) or (self.left is not None and self.right is None):
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

        
        def _recurse(node: BSTNode, value):
            
            if node is None:
                return None
            
            if value < node.value:
                node.left = _recurse(node.left, value)

            elif value > node.value:
                node.right = _recurse(node.right, value)
            
            # node found, value == node.value
            else:
                
                 if node.left is None and node.right is None:
                     node = None
            
                # one child, either left or right, successor take over
                 elif node.has_one_child():
                     if node.left is not None:
                         return node.left
                     else:
                        return node.right
                 
                 # # both left and right children
                    # get either largest value of left node or smallest value of right node
                    # update node-to-del value with replace largest or smallest
                    # delete largest or smallest node by recursively going through same process
                 else:
                     
                     min_node_of_right_tree = self._find_min_value(node.right)
                     
                     node.value = min_node_of_right_tree.value
                     
                     # delete min node of right
                     temp = _recurse(min_node_of_right_tree, min_node_of_right_tree.value)
                     node.right = temp
            
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
            #     largest_node_on_left = self._find_max_value(node_to_del.left)
                
            #     node_to_del = largest_node_on_left
                
            #     # now to delete largest node on left
            #     _recurse(largest_node_on_left.value)
                
                
        _recurse(self.root, value)
        
    
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
        
        
    
    #https://www.youtube.com/watch?v=fAAZixBzIAI&t=1422s
    def sum_with_recursion(self): 
        
        if self.root is None:
            return 0
        
        totalSum = 0
        
        def _recurse(node):
            nonlocal totalSum
            
            if node is None:
                return 0

            totalSum += node.value
            
            _recurse(node.left)
            
            _recurse(node.right)
            
            return totalSum
            
        
        _recurse(self.root) + self.root.value
        
        return totalSum
    
    def sum_with_breadth_first_search(self):
        
        queue = []
        totalSum = 0
        
        queue.append(self.root)
        
        while len(queue) > 0:
            
            current_node = queue.pop()
            
            totalSum += current_node.value
            
            if current_node.left is not None:
                queue.append(current_node.left)
                
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return totalSum
        
        
    
    def min(self) -> BSTNode:
        
        node = self._find_min_value(self.root.left)
        return node
    
    def max(self) -> BSTNode:
        
        node = self._find_max_value(self.root.right)
        return node
    
    
    def _find_min_value(self, node) -> BSTNode:
        
        if node.left is None:
            return node
        
        return self._find_min_value(node.left)
        
    
    def _find_max_value(self, node) -> BSTNode:
        
        
        if node.right is None:
            return node
        
        return self._find_max_value(node.right)
    
    # depth of tree from root to last level leaf node
    def height(self):
        
        def _recurse(node):
            
            # my style
            # if node is None:
            #     return 0
            
            # leftHeight = _recurse(node.left) + 1
            
            # rightHeight = _recurse(node.right) + 1
            
            # maxHeight = max(leftHeight, rightHeight)
            
            # return maxHeight
            
            # simplified style
            if node is None:
                return 0
            
            return max(_recurse(node.left), _recurse(node.right)) + 1
            
            
        height = _recurse(self.root)
        
        return height
        

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
    bst.insert(4)
    bst.insert(1)
    
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
    
    #bst.delete(6)
    # print(bst.min().value)
    
    # print(bst.max().value)
    
    # print(bst.height())
    
    # print(bst.sum_with_breadth_first_search())
    
    # print(bst.sum_with_recursion())
    
    
    
    # depth first search
    # dfs = DFS()
    # dfs.search(0)
    
    # bfs = BFS()
    # path, distant = bfs.traverse(1, 6)
    # print(f'distant: {distant}, {path}')
    
    # find_max_subarray_nums = [4,2,1,7,8,1,2,8,1,0]
    # find_max_subarray(find_max_subarray_nums, 3)
    
    # smallest_sub_array_size_nums = [4,2,2,7,8,1,2,8,1,0]
    # find_smallest_sub_array_size(smallest_sub_array_size_nums)
    
    # adjacencyMatrix = AdjacencyMatrix()
    # adjacencyMatrix.dfs(0)
    
    binarySearch = BinarySearch()
    found, index = binarySearch.search(2)
    print(found)
    
    