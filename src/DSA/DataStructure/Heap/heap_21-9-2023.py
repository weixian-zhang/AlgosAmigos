
import math
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
    
    def bottom_up_heapify(self, nums):
        pass
    
    def build_max_heap(self, numsArr):
        
        # get starting point to heapify, last internal node before any leave node starts
        startIdx = math.ceil(len(numsArr) / 2) - 1
        
        for idx in range(startIdx, -1, -1):
            self.top_down_heapify_max(numsArr, idx)
            
        return numsArr
    
    def build_min_heap(self):
        pass
    
    def insert(self, val):
        pass
    
    def delete(self, val):
        pass
    
    def _swap(self, numsArr, src, dest):
        temp = numsArr[src]
        numsArr[src] = numsArr[dest]
        numsArr[dest] = temp
        
        
    
    
if __name__ == '__main__':
    
    nums = [1,2,6,14,8,7]
    
    heap = Heap()
    
    maxHeap = heap.build_max_heap(nums)
    
    print(maxHeap)
    

