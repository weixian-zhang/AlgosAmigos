class Solution:
    
    # neetcode soluton - use Set to remove duplicate and lookup O(1)
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numsSet = set(nums)
        longest = 0
        
        for x in nums:
            
            if not x - 1 in nums:
                consec = 0
                
                while consec in numsSet:
                    consec += 1
                    
                longest = max(longest, consec)
        
        return longest
    
    # my solution with a Set to remove duplicate, sort list and sliding window
    # time: O(n) - sort + sliding window
    # space: O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        
        dupRemover = list(set(nums))
        dupRemover.sort()
        nums = dupRemover
        
        maxSub = 0
        left, right = 0, 1
        lastIndex = len(nums) - 1
        
        while left <= lastIndex and right <= lastIndex:
            
            if nums[right] - 1 == nums[right - 1]:
                right += 1
            else:
                consecSub = ((right - 1) - left) + 1
                maxSub = max(maxSub, consecSub)
                left = right
                right += 1
        
        if right > left:   
            consecSub = ((right - 1) - left) + 1
            maxSub = max(maxSub, consecSub)
                
        return maxSub
    
    

s = Solution()
# print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,2,0,1]))