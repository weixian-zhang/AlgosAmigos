class QueueItem:
    def __init__(self, data, priority) -> None:
        self.data = data
        self.priority = priority
    
class PriorityQueue:
    
    def __init__(self) -> None:
        self.pq: list[QueueItem] = []
        self.minheap = MinHeap()
    
    def enqueue(self, data, priority):
        
        item = QueueItem(data, priority)
        
        self.minheap.insert(self.pq, item)
    
    def dequeue(self) -> QueueItem:
        item = self.minheap.delete(self.pq)
        return item
    
    
    def peek(self) -> QueueItem:
        
        """returns the highest priority item without removing it
        """
        
        if self.pq == []:
            return None
        
        return self.pq[0]

    

class MinHeap:
    
    def build_heap(self, pq: list[QueueItem]):
        
        last_internal_node_idx = (len(pq) // 2) - 1
        
        for x in range(last_internal_node_idx, -1, -1):
            self.top_down_heapify(pq, x)
    
    # used for pq.enqueue
    def insert(self, pq: list[QueueItem], item: QueueItem):
        
        pq.append(item)
        
        self.bottom_up_heapify(pq, len(pq) - 1)
    
    # used for pq.dequeue
    def delete(self, pq: list[QueueItem]) -> QueueItem:
        
        self._swap(pq, 0, len(pq)-1)
        
        result = pq.pop()
        
        self.top_down_heapify(pq, 0)
        
        return result
        
    
    def top_down_heapify(self, pq: list[QueueItem], idx: int):
        
        smallestIdx = idx
        leftIdx = 2 * idx + 1
        rightIdx = 2 * idx + 2
        
        if leftIdx <= len(pq) - 1 and pq[leftIdx].priority < pq[smallestIdx].priority:
            smallestIdx = leftIdx
            
        if rightIdx <= len(pq) - 1 and pq[rightIdx].priority < pq[smallestIdx].priority:
            smallestIdx = rightIdx
            
        if smallestIdx != idx:
            self._swap(pq, idx, smallestIdx)
            self.top_down_heapify(pq, smallestIdx)
            
    
    def bottom_up_heapify(self, pq: list[QueueItem], idx: int):
        
        parentIdx = (idx - 1) // 2
        
        if parentIdx >= 0 and parentIdx <= len(pq) - 1:
        
            if pq[parentIdx].priority > pq[idx].priority:
                self._swap(pq, parentIdx, idx)
                self.bottom_up_heapify(pq, parentIdx)
            
            
    def _swap(self, pq: list[QueueItem], src, dest):
        temp = pq[src]
        pq[src] = pq[dest]
        pq[dest] = temp
        
        
if __name__ == '__main__':
    
    pq = PriorityQueue()
    
    pq.enqueue(10, 10)
    print([x.priority for x in pq.pq])
    pq.enqueue(8, 8)
    print([x.priority for x in pq.pq])
    pq.enqueue(7, 7)
    print([x.priority for x in pq.pq])
    pq.enqueue(2, 2)
    print([x.priority for x in pq.pq])
    pq.enqueue(1, 1)
    print([x.priority for x in pq.pq])
    pq.enqueue(6, 6)
    print([x.priority for x in pq.pq])
    
    prioritizedItem = pq.peek()
    print(f'peek highest priority item at priority: {prioritizedItem.priority}')
    
    print(pq.dequeue().priority)
    print(pq.dequeue().priority)
    print(pq.dequeue().priority)
    print(pq.dequeue().priority)
    print(pq.dequeue().priority)
    print(pq.dequeue().priority)