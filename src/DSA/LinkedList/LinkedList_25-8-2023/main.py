
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        

class LinkedList:
    
    def __init__(self) -> None:
        self._head = None
        
    def add(self, data: int) -> None:
        
        if self._head is None:
            self._head = Node(data)
        else:
            last_node, _ = self._traverse_to_end_node()
            last_node.next = Node(data)
    
    
    def delete(self, data: int) -> None:
        
        if self._head is None:
            return None
        
        temp: Node = self._head
        prev: Node = None
        
        def _delete( temp, prev):
        
            
            if temp.next is None:
                if temp.data == data and prev is not None:
                    prev.next = None
                else:
                    self._head = None
                return
        
            if temp.data == data:
                if temp.next is None:
                    prev.next = None
                    return
                else:
                    prev.next = temp.next
                    return
            
            prev = temp
            temp = temp.next
            
            _delete(temp, prev)
            
            
        _delete(self._head, prev)
            
        
        # while temp.next is not None:
            
        #     if temp.data == data:
        #         prev.next = temp.next
        #         temp = None
        #         return
            
        #     prev = temp
        #     temp = temp.next
            
        # if temp.data == data:
        #     if temp is not None:
        #         prev.next = temp
        #     else:
        #         prev.next = None
            
        
    
    def search(self, data: int) -> Node:
        result = self._search(data)
        return result
    
    def length(self) -> int:
        _, count = self._traverse_to_end_node()
        return count
    
    
    def _search(self, data):
        
        if self._head is None:
            return None
        
        temp = self._head
        
        while temp is not None:
            
            if temp.data == data:
                return temp
            
            if temp.next is not None:
                temp = temp.next
                
        return None
    
    def _traverse_to_end_node(self) -> Node:
        
        if self._head is None:
            return None, 0
        
        count = 1
        temp = self._head
        
        while temp.next is not None:
            
            count += 1
            temp = temp.next
            
        return temp, count
    
    
if __name__ == '__main__':
    
    ll = LinkedList()
    
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)
    
    print(ll.length())
    
    ll.delete(20)
    
    print(ll.length())
    
    ll.delete(40)
    
    ll.delete(30)
    
    ll.delete(10)
    
    print(ll.length())
    