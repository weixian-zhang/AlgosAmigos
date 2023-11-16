from collections import OrderedDict

class MinStack:

    def __init__(self):
        self.stack = []
        self.minMap = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        idxKey = len(self.stack) - 1
        self.minMap[idxKey] = val

        self._sort_minmap()

    def pop(self) -> None:
        del self.minMap[len(self.stack) - 1]
        self.stack.pop()
        self._sort_minmap()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minMap[list(self.minMap.keys())[0]]
    
    def _sort_minmap(self):
        self.minMap = OrderedDict(sorted(self.minMap.items(), key= lambda item: item[1]))

    # def _heapify_min(self):
        
    #     def _recurse(nums: list[int], idx):
            
    #         smallest = idx
    #         leftChild = 2 * idx + 1
    #         rightChild = 2 * idx + 2

    #         if leftChild <= len(nums) -1 and nums[leftChild] < nums[smallest]:
    #             smallest = leftChild

    #         if rightChild <= len(nums) -1 and nums[rightChild] < nums[smallest]:
    #             smallest = rightChild

    #         # swap
    #         if idx!= smallest:
    #             nums[idx], nums[smallest] = nums[smallest], nums[idx]
    #             _recurse(nums, smallest)
            

    #     lastNodeIndexWithLeaves = (len(self.minHeap) // 2) - 1

    #     for x in range(lastNodeIndexWithLeaves, -1, -1):
    #         _recurse(self.minHeap, x)


    # def _heapify_min_delete(self,popIdx):
    #     self.minHeap[popIdx], self.minHeap[-1] = self.minHeap[-1], self.minHeap[popIdx]
    #     self.minHeap.pop()
    #     self._heapify_min()

    # def _heapify_min_add(self, num):
    #     self.minHeap.append(num)
    #     self._heapify_min()


# Your MinStack object will be instantiated and called as such:
# ["MinStack","push","push","push","getMin","top","pop","getMin"]
# [[],[-2],[0],[-1],[],[],[],[]]
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-1)
# print(minStack.getMin()) # return -2
# print(minStack.top());   # return -1
# minStack.pop()
# print(minStack.getMin()) # return -2

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin()) # return -3
# minStack.pop()
# print(minStack.top());   # return -1
# print(minStack.getMin()) # return -2

# ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
# [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.getMin()) # return -2
minStack.pop()
print(minStack.getMin()) # return -2