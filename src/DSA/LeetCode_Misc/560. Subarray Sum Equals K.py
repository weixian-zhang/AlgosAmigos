class Solution:

    # brute force - TLE
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        N = len(nums)
        count = 0

        for i in range(N):
            tempSum = nums[i] 
            if nums[i] == k:
                count += 1
            for j in range(i + 1, N):
                tempSum += nums[j]
                if tempSum == k:
                    count += 1

        return count


    # prefix sum + reverse math Sum - K the nkeep track of prefix sum count
    def subarraySum(self, nums: list[int], k: int) -> int:

        N = len(nums)

        subarrays = 0
        prefixSum = 0
        cumuSums = {}

        for x in range(N):

            prefixSum += nums[x]

            if prefixSum == k:
                subarrays += 1

            if (prefixSum - k) in cumuSums:
                subarrays += cumuSums[prefixSum - k]
            
            if prefixSum not in cumuSums:
                 cumuSums[prefixSum] = 1 
            else:
                cumuSums[prefixSum] += 1

        return subarrays


s = Solution()
# print(s.subarraySum([100,1,2,3,100,1,2,3,4], 3))
# print(s.subarraySum([5, 0, 0, 0, 2, 3], 0))
# print(s.subarraySum([100,1,2,3,4], 6)) # 1
print(s.subarraySum([1, -1, 0], 0))     # 3
# print(s.subarraySum([1], 1))
# print(s.subarraySum([-1, -1, 1], 0))
# print(s.subarraySum([1], 0))
# print(s.subarraySum([1,1,1], 2))
# print(s.subarraySum([1,2,3], 3))
# print(s.subarraySum([1,7,4,3,5,0,2,10], 7))