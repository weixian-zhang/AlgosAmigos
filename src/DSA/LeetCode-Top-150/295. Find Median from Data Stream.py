import heapq

# always sorting O(N) - Time Limit Exceeded
# class MedianFinder:

#     def __init__(self):
#         self.nums = []

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)
#         self.nums.sort()

#     def findMedian(self) -> float:

#         N = len(self.nums)

#         if N == 0:
#             return None
#         if N== 1:
#             return self.nums[0]
        
#         mid = len(self.nums) // 2

#         if N % 2 == 0:
#             midPrev = mid - 1
#             return (self.nums[mid] + self.nums[midPrev]) / 2
#         else:
#             return self.nums[mid]

        
class MedianFinder:

    def __init__(self):
        self.count = 0
        self.smallMaxHeap = [] # max heap. num in this list is smaller than largeMinHeap
        self.largeMinHeap = [] # min heap

    def addNum(self, num: int) -> None:
    

        heapq.heappush(self.smallMaxHeap, -1 * num)

        # make sure every element in small heap is smaller than large heap
        if (self.smallMaxHeap and self.largeMinHeap and (-1 * self.smallMaxHeap[0]) > self.largeMinHeap[0]):
            val = -1 * heapq.heappop(self.smallMaxHeap)
            heapq.heappush(self.largeMinHeap, val)

        if len(self.smallMaxHeap) > len(self.largeMinHeap) + 1:
           val = -1 * heapq.heappop(self.smallMaxHeap)
           heapq.heappush(self.largeMinHeap, val)
        
        if len(self.largeMinHeap) > len(self.smallMaxHeap) + 1:
           val = heapq.heappop(self.largeMinHeap)
           heapq.heappush(self.smallMaxHeap, -1 * val)



    def findMedian(self) -> float:

        # is even number of nums
        if len(self.smallMaxHeap) > len(self.largeMinHeap):
            return -1 * self.smallMaxHeap[0]
            
        if len(self.largeMinHeap) > len(self.smallMaxHeap):
            return self.largeMinHeap[0]

        return ((-1 * self.smallMaxHeap[0]) + self.largeMinHeap[0]) / 2 
        
            

        
            


mf = MedianFinder()

#print(mf.findMedian())
# mf.addNum(3)
# # print(mf.findMedian())
# mf.addNum(2)
# # print(mf.findMedian())
# mf.addNum(7)
# # print(mf.findMedian())
# mf.addNum(5)

mf.addNum(6)
print(mf.findMedian())
mf.addNum(10)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
mf.addNum(6)
print(mf.findMedian())
mf.addNum(5)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
mf.addNum(6)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
mf.addNum(1)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
# mf.addNum(-3)
print(mf.findMedian())
mf.addNum(-4)
print(mf.findMedian())
mf.addNum(-5)
print(mf.findMedian())

            

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()