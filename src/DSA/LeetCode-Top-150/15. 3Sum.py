class Solution:

    # 3 pointers
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        result = {}
        lastIdx = len(nums) - 1

        for i, n in enumerate(nums):
    
            l2, r = i + 1, lastIdx
            while l2 < r:
                
                if n + nums[l2] + nums[r] > 0:
                    r -= 1
                elif n + nums[l2] + nums[r] < 0:
                    l2 += 1
                else:
                    self._add_unique(result, [n, nums[l2], nums[r]])
                    r -= 1
        
        return list(result.values())

    def _add_unique(self, result: dict, args):

        args.sort()
        numsKey = ''.join([str(x) for x in args])
        if numsKey not in result:
            result[numsKey] = args







s = Solution()
print(s.threeSum([-2,0,1,1,2]))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))