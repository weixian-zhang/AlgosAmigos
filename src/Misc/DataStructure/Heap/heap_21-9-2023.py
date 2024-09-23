

class Heap:
    
    def add(self, nums: list[int], num):
        
        nums.append(num)
        
        self.heapify_max(nums)
        
    
    def delete(self, nums: list[int], num=None):
        
        index = -1
        
        if num is None:
            index = 0
        else:
            for idx, x in enumerate(nums):
                if x == num:
                    index = idx
                    break
                
        if index != -1:
            nums[index], nums[-1] = nums[-1], nums[index]
            nums.pop()
            self.heapify_max(nums)

    def _heapify_up(nums, idx):
        pass

    def _heapify_down(nums, idx):
        pass
            
    
    def heapify_max(self, nums: list[int], index: int = -1):
        
        def _heapify_max(nums: list[int], index):
        
            numLen = len(nums)-1
            largest = index
                
            leftChild = 2 * largest + 1
            rightChild = 2 * largest + 2
            
            if leftChild <= numLen and nums[leftChild] > nums[largest]:
                largest = leftChild
                
            if rightChild <= numLen and nums[rightChild] > nums[largest]:
                largest = rightChild
                
            if largest != index:    
                nums[index],  nums[largest] = nums[largest], nums[index]
                _heapify_max(nums, largest)
        
        
        if index == -1:
            # find last internal node with leave node(s)
            lastInternalNodeIdx = (len(nums) // 2) - 1
            
        for x in range(lastInternalNodeIdx, -1, -1):
            _heapify_max(nums, x)
            
    
    def heapify_min(self, nums: list[int]):
     
        def _heapify_min(nums: list[int], index: int):
                  
            smallest = index
            
            numLen = len(nums)-1
            
            leftChild = 2 * smallest + 1
            rightChild = 2 * smallest + 2
            
            if leftChild <= numLen and nums[leftChild] < nums[smallest]:
                smallest = leftChild
                
            if rightChild <= numLen and nums[rightChild] < nums[smallest]:
                smallest = rightChild
                
            if smallest != index:
                nums[index], nums[smallest] = nums[smallest], nums[index]
                _heapify_min(nums, smallest)
                
        
        lastInternalNodeIndex = (len(nums) // 2) - 1
        
        for x in range(lastInternalNodeIndex, -1, -1):
            _heapify_min(nums, x)
            
            


nums = [1,2,3,4,5,9]

heap = Heap()

heap.heapify_max(nums)
print(nums)

# heap.heapify_min(nums)
# print(nums)

heap.add(nums, 20)
print(nums)

heap.delete(nums, 9)
print(nums)

heap.delete(nums)
print(nums)

heap.heapify_min(nums)
print(nums)


# import heapq
# heapq._heapify_max(nums)
# print(nums)

    