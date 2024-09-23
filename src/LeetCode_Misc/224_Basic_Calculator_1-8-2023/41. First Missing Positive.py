class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        # Implement your solution here

        # set find, insert, del is O(1) as set is using dict/hashmap under the hood
        nums = set(nums)
        min = 1

        while min in nums:
            min += 1

        return min
    
s = Solution()
s.firstMissingPositive([-1,-2,-60,40,43])