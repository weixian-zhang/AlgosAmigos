from typing import List
from queue import PriorityQueue

# brute force - Memory limit exceeded
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        allCombos = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                n1 = nums1[i]
                n2 = nums2[j]
                
                allCombos.append((n1 + n2, n1, n2))

        sortedNums = sorted(allCombos, key=lambda tup: tup[0])
        result = []

        for x in range(k):
            n1 = sortedNums[x][1]
            n2 = sortedNums[x][2]
            result.append([n1, n2])

        return result

# brute force with PriorityQueue - Memory limit exceeded
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        q = PriorityQueue()

        def get_pairs():
            nonlocal q

            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    n1 = nums1[i]
                    n2 = nums2[j]
                    q.put((n1 + n2, [n1, n2]))

        get_pairs()

        result = []

        while q.queue:
            result.append(q.get()[1])

            if len(result) == k:
                break

        return result
    
# Larry's solution
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq

        N1 = len(nums1) - 1 
        N2 = len(nums2) - 1

        minHeap = []
        result = []
        i, j = 0, 0
        visited = set()
      
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))

        while len(minHeap) > 0 and k > 0:
        
            _, i, j = heapq.heappop(minHeap)
            
            result.append([nums1[i], nums2[j]])
            
            if i + 1 <= N1 and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 <= N2 and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))


            if i + 1 <= N1 and j + 1 <= N2 and (i+1, j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j + 1], i + 1, j + 1))
                visited.add((i + 1, j + 1))

            k -= 1


        return result
        


s = Solution()

print(s.kSmallestPairs([1,2,4,5,6],[3,5,7,9],20))
# print(s.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3))
# print(s.kSmallestPairs([1,1,2], [1,2,3], 2))
# print(s.kSmallestPairs([1,7,11], [2,4,6], 3))