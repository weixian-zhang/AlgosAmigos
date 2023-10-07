class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        if k > len(nums):
            return -1
        
        lastInternalNode = (len(nums) // 2) - 1
        
        heap = nums.copy()
        
        for x in range(lastInternalNode, -1, -1):
            self.heapify(heap, x)
            
        for x in range(k-1):
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            self.heapify(heap, 0)
               
        return heap[0]
        
    def heapify(self, nums, nodeIdx):
        
        largest = nodeIdx
        
        leftChild = nodeIdx * 2 + 1
        
        rightChild = nodeIdx * 2 + 2
        
        
        if leftChild < len(nums) and nums[leftChild] > nums[largest]:
            largest =leftChild
        
        if rightChild < len(nums) and nums[rightChild] > nums[largest]:
            largest = rightChild
            
        if largest != nodeIdx:
            nums[nodeIdx], nums[largest] = nums[largest], nums[nodeIdx]
            self.heapify(nums, largest)
            

    
    
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))