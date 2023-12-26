class Solution:

    # brute force - TLE
    def maxProduct(self, nums: list[int]) -> int:
        
        N = len(nums)
        maxProd = -10 ** 10

        for i in range(N):
            tempProd = nums[i]
            maxProd = max(maxProd, tempProd)
            for j in range(i + 1, N):
                tempProd *= nums[j]
                maxProd = max(maxProd, tempProd)

        return maxProd
    
    # bottom up DP
    def maxProduct(self, nums: list[int]) -> int:

        #nums = [1] + nums   # add dummy 1 in front
        N = len(nums)
        result = 1
        maxSoFar = 1
        minSoFar =  1

        for x in nums:
            if x == 0:
                maxSoFar, minSoFar = 1, 1
                continue

            current = x

            tempMaxSoFar = current * maxSoFar   # store maxSoFar before it gets overriden in next line

            maxSoFar = max(current * 1, current * maxSoFar, current * minSoFar)

            minSoFar = min(current * 1, tempMaxSoFar, current * minSoFar)

            result = max(result, minSoFar, maxSoFar)

        return result
                

        


s = Solution()
print(s.maxProduct([2,-5,-2,-4,3]))
# print(s.maxProduct([-2, 0, -1]))
# print(s.maxProduct([0, 2]))
# print(s.maxProduct([2,3,-2,4]))