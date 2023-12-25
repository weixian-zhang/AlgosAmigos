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
                

        


s = Solution()
# print(s.maxProduct([0, 2]))
print(s.maxProduct([2,3,-2,4]))