
#https://afteracademy.com/blog/operations-on-heaps/

class Heap:
    
    def top_down_heapify_max(self, nums, idx):
        
        largest = idx
        leftIdx = 2*idx + 1
        rightIdx = 2*idx + 2
        
        if leftIdx <= (len(nums) - 1) and nums[largest] < nums[leftIdx]:
            largest = leftIdx
            
        
        if rightIdx <= (len(nums) - 1) and nums[largest] < nums[rightIdx]:
            largest = rightIdx
            
        if largest != idx:
            self._swap(nums, idx, largest)
            #nums[idx], nums[largest] = nums[largest], nums[idx]
            self.top_down_heapify_max(nums, largest)
    
    def bottom_up_heapify_max(self, nums, idx):
        
        parentIdx = (idx - 1) // 2
        
        if nums[parentIdx] < nums[idx]:
            self._swap(nums, idx, parentIdx)
            self.bottom_up_heapify_max(nums, parentIdx)
    
    def build_max_heap(self, numsArr):
        
        # get starting point to heapify, last internal node before any leave node starts
        startIdx = (len(numsArr) // 2) - 1
        
        for idx in range(startIdx, -1, -1):
            self.top_down_heapify_max(numsArr, idx)
            
        return numsArr
    
    
    def top_down_heapify_min(self, nums, idx):
        
        numsLen = len(nums) - 1
        smallest = idx
        leftChildIdx = 2 * idx + 1
        rightChildIdx = 2 * idx + 2
        
        if leftChildIdx <= numsLen and nums[smallest] > nums[leftChildIdx]:
            smallest = leftChildIdx
            
        if rightChildIdx <= numsLen and nums[smallest] > nums[rightChildIdx]:
            smallest = rightChildIdx
            
        if smallest != idx:
            self._swap(nums, idx, smallest)
            self.top_down_heapify_min(nums, smallest)
        
    
    def bottom_up_heapify_min(self, nums, idx):
        
        parentIdx = (idx - 1) // 2
        
        if nums[idx] < nums[parentIdx]:
            self._swap(nums, idx, parentIdx)
            self.bottom_up_heapify_min(nums, parentIdx)
    
    def build_min_heap(self, nums):
        
        last_internal_node_idx = (len(nums) // 2) - 1
        
        for x in range(last_internal_node_idx, -1, -1):
            self.top_down_heapify_min(nums, x)
            
        return nums
    
    def insert(self, nums: list[int], val, isMax=True):
              
        nums.append(val)
        
        if isMax:
            self.bottom_up_heapify_max(nums, len(nums) - 1)
        else:
            self.bottom_up_heapify_min(nums, len(nums) - 1)
            
    
    def delete(self, nums, isMax=True):
        
        lastIdx = len(nums)-1
        
        # swap first to last item
        self._swap(nums, 0, lastIdx)
        
        # delete last item (which was root before)
        nums.pop()
        
        if isMax:
            self.top_down_heapify_max(nums, 0)
        else:
            self.top_down_heapify_min(nums, 0)
        
        
    
    def _swap(self, numsArr, src, dest):
        temp = numsArr[src]
        numsArr[src] = numsArr[dest]
        numsArr[dest] = temp
        
        
    
    
if __name__ == '__main__':
    
    nums = [1,2,6,14,8,7]
    
    heap = Heap()
    
    # test max heap
    maxHeap = heap.build_max_heap(nums)
    
    print(maxHeap)
    
    heap.insert(nums, 10)
    
    print(maxHeap)
    
    heap.delete(nums)
    
    print(maxHeap)
    
    # test min heap
    
    minHeap = heap.build_min_heap(nums)
    
    print(minHeap)
    
    heap.insert(minHeap, 5, isMax=False)
    
    print(minHeap)
    
    heap.delete(minHeap, isMax=False)
    
    print(minHeap)
    

