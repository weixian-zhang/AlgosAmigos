       

# implement link link delete at position

# linked list recursion
# https://www.youtube.com/watch?v=8GtdXAqaQHg

# reverse linked list with recursion
# https://leetcode.com/problems/reverse-linked-list-ii/editorial/?envType=study-plan-v2&envId=top-interview-150

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert(self, val):
        
        if self.head is None:
            self.head = TreeNode(val)
            return
        
        current = self.head
        
        while current.next is not None:
            current = current.next
            
        current.next = TreeNode(val)
        
        
    def insert_at(self, position: int, val: int):
        
        if self.head is None:
            self.head = TreeNode(val)
            return
        
        if position == 1:
            newNode = TreeNode(val)
            newNode.next = self.head
            self.head = newNode
            return
        
        pos = 1
        current = self.head
        prev = current
        
        while current is not None:
            
            if pos == position:
                newNode = TreeNode(val)
                
                prev.next = newNode
                newNode.next = current                
                return
            
            prev = current
            current = current.next
            pos += 1
        
        # if position larger than 
        print('posotion exceed LinkedList nodes')
    
    
    def delete_at(self, position: int):
        
        pos = 1
        current = self.head
        prev = current
        
        if position == 1:
            self.head = self.head.next
            return
        
        while current is not None:
            
            if pos == position:
                prev.next = current.next
                return
            
            prev = current
            current = current.next
            pos += 1
            
    def display(self, node=None):
        
        result = []
        
        if node is not None:
            current = node
        else:
            current = self.head
        
        while current is not None:
            result.append(current.val)
            current = current.next
            
        print('->'.join([str(x) for x in result]))
        
        
    def list_to_linkedlist(self, arr):
        
        dummy = TreeNode(-100000)
        
        current = dummy
        
        for x in arr:
            current.next = TreeNode(x)
            current = current.next
            
        return dummy.next
    
    
    def sum(self):
        
        def _sum_recurse(node, sum):
            
            if node is None:
                return sum
            
            sum += node.val + _sum_recurse(node.next, sum)
            
            return sum
        
        
        return _sum_recurse(self.head, 0)
            
            
if __name__ == '__main__':
    
    ll = LinkedList()
    
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    
    print(ll.sum())
    
    # ll.display()
    
    # ll.delete_at(4)
    
    # ll.display()
    
    # ll.delete_at(1)
    
    # ll.display()
    
    # ll.delete_at(1)
    
    # ll.display()
    
    # ll.insert_at(1,1)
    
    # ll.insert_at(2,2)
    
    # ll.insert_at(3,3)
    
    # ll.insert_at(4,4)
    
    # ll.display()
    
    # node = ll.list_to_linkedlist([10,20,30,40,50,60,70])
    
    # ll.display(node)
    
    
    
    
    