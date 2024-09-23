
#Node
class Node:    
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = Node(0,0)  # head is the least recently used
        self.tail: Node = Node(0,0)   # tail is the most recently used
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    # insert to right, right is latest
    def insert(self, newNode):
        # if self.head is None:
            
        #     self.head = newNode
        #     self.tail = newNode
        #     self.head.next = self.tail
        #     self.tail.prev = self.head
            
        #     self.count += 1
            
        #     return newNode
        
        #tail = self.tail
        prevTail = self.tail.prev
        newNode.prev = prevTail
        self.tail = newNode
        
        # prevNew = self.tail
        # prevNew.next = newNode
        # newNode.prev = prevNew
        
        # self.head.next = newNode
        # self.tail = newNode
        
        self.count += 1
        
        return newNode
    
    # head is the least recently used
    def delete_head(self) -> int:
        if self.head is None:
            return
        
        leastRecentlyUsedKey = self.head.key
        
        
        
        if self.head.next is not None:
            newHead = self.head.next
            self.head = newHead
        
        
        self.head.prev = None
        
        self.count -= 1
        
        return leastRecentlyUsedKey
    
    def make_node_most_recent(self, nodeToMk):
        
        if self.tail.key == nodeToMk.key:
            return
    
        
        nodeToMk_Prev = nodeToMk.prev
        nodeToMk_Next = nodeToMk.next
        
        # is node head
        
        mrNode = self.tail
        
        if self.head.key == nodeToMk.key and self.head.next is not None:
            self.head = nodeToMk_Next            
        else:
            if nodeToMk_Prev is not None and nodeToMk_Next is not None:
                nodeToMk_Prev.next = nodeToMk_Next
            if nodeToMk_Next is not None and nodeToMk_Prev is not None:
                nodeToMk_Next.prev = nodeToMk_Prev  
        
        nodeToMk.next = None    # most recent node, next must be None
        
        mrNode.next = nodeToMk
        nodeToMk.prev = mrNode
        
        self.tail = nodeToMk
    
    
    
    def to_list(self):
        result = []
        
        n = self.head
        
        result.append(n.key)
        
        while n.next is not None:
            n = n.next
            result.append(n.key)
            
        return result


class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.ddl = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            
            node = self.cache[key]
            
            # make Node be "latest"
            self.ddl.make_node_most_recent(node)
            
            return node.value

            
        
        return -1
       
        

    def put(self, key: int, value: int) -> None:
        
        newNode = Node(key, value)
        
        if key in self.cache:
            existingNode = self.cache[key]
            existingNode.value = value

            self.ddl.make_node_most_recent(existingNode)
            return
        
        if self.ddl.count + 1 > self.capacity:
                
            # delete least recently used node
            oldKey = self.ddl.delete_head()
                
            if oldKey in self.cache:
                self.cache.pop(oldKey)
            
            insertedNode = self.ddl.insert(newNode)
            
            self.cache[key] = insertedNode
                
        else:
            
            insertedNode = self.ddl.insert(newNode)
            
            self.cache[key] = insertedNode
                