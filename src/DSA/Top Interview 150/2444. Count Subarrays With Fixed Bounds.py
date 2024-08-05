class Solution:

    # brute force - TLE
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == minK and nums[i] == maxK:
                    count += 1
            for j in range(i + 1, len(nums)):
                if min(nums[i:j + 1]) == minK and max(nums[i:j + 1]) == maxK:
                    count += 1

        return count
    
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
         
         
         nums.append(10 ** 20)
        
        # larry's
        #  def solve(arr):
        #       N = len(arr)
        #       count = 0

        #       lastMin, lastMax = -1, -1

        #       for i in range(N):
        #            if arr[i] == minK:
        #                 lastMin = i
        #            if arr[i] == maxK:
        #                 lastMax = i

        #            count += min(lastMin, lastMax) + 1

        #       return count
         
         def solve(arr):
              
              N = len(arr)
              lastMin = lastMax = -1
              minFound = maxFound = False
              subarrCount = [0 for x in range(N)]


              for x in range(N):
                   if arr[x] == minK:
                        minFound = True
                        lastMin = x
                   if arr[x] == maxK:
                        maxFound = True
                        lastMax = x

                   if minFound and maxFound:
                        subarrCount[x] = subarrCount[x - 1] + min(lastMin, lastMax) + 1

              return subarrCount[-1]


         arr = []
         count = 0

         for x in nums:

              if minK <= x <= maxK:
                   arr.append(x)
              else:
                   count += solve(arr)
                   arr = []
        

         return count





s = Solution()
# print(s.countSubarrays([2,5,1,3,5,2], 1, 5))
# print(s.countSubarrays([1,3,8,5,4,3,1,1], 1, 5))
print(s.countSubarrays([35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913],
                        35054, 
                        945315))
# print(s.countSubarrays([1,3,5,2,7,5], 1, 5))
# print(s.countSubarrays([1,1,1,1], 1, 1))