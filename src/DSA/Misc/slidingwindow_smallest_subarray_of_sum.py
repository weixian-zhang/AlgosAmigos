class Solution:
    
    def smallestSubArrayOfSum(self, nums: list[int], sumNum: int):
        
        subarrSize = 10 ** 20
        start = end = 0

        while end <= len(nums):

            if sum(nums[start : end + 1]) == sumNum:
                subarrSize = min(subarrSize, (end - start) + 1)
                start = end
                end += 1
            elif sum(nums[start : end + 1]) < sumNum:
                end += 1
            else:
                start += 1

        return subarrSize
    


s = Solution()
# print(s.smallestSubArrayOfSum([1,2,3,4,5,6], 7))
print(s.smallestSubArrayOfSum([1,2,3,4,7, 5,6], 7))
