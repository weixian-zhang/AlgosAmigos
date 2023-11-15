class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._heapify_min_add(val)

    def pop(self) -> None:
        self.stack.pop()
        self._heapify_min_delete()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[0]

    def _heapify_min(self):
        
        def _recurse(nums: list[int], idx):
            
            smallest = idx
            leftChild = 2 * idx + 1
            rightChild = 2 * idx + 2

            if nums[leftChild] < nums[smallest]:
                smallest = leftChild

            if nums[rightChild] < nums[smallest]:
                smallest = rightChild

            # swap

            if idx!= smallest:
                nums[idx], nums[smallest] = nums[smallest], nums[idx]
                _recurse(nums, smallest)
            

        lastNodeIndexWithLeaves = (len(self.minHeap) // 2) - 1

        for x in range(lastNodeIndexWithLeaves, -1, -1):
            _recurse(self.minHeap, x)


    def _heapify_min_delete(self, idx):
        self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
        self.minHeap.pop()
        self._heapify_min()

    def _heapify_min_add(self, num):
        self.minHeap.append(num)
        self._heapify_min()


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top();   # return 0
minStack.getMin() # return -2