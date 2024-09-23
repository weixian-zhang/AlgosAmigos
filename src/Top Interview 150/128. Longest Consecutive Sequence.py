# Runtime: 377 ms, faster than 85.35% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 32.5 MB, less than 15.87% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        nums = list(set(nums))
        nums.sort()

        lc = 0
        left, right = 0, 1

        while right <= len(nums) - 1:
            if nums[right] - 1 == nums[right - 1]:
                right += 1
            else:
                lc = max(lc, (right - left))
                left = right
                right += 1

        return max(lc, (right - left))
    
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))