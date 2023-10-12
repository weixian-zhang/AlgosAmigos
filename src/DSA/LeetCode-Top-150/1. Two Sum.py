class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diffIdx = {}
        
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff not in diffIdx:
                diffIdx[nums[x]] = x
            else:
                
                return [diffIdx[diff], x]
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))