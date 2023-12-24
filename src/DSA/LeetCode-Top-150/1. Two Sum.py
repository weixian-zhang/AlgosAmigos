class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diffMap = {}
        N = len(nums)

        for x in range(N):
            diff =  target - nums[x]
            if nums[x] not in diffMap:
                diffMap[diff] = x
            else:
                return [diffMap[nums[x]], x]



s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))