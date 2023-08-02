class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        prev_seen = {}
        
        for idx in range(len(nums)):
            
            if nums[idx] > target:
                continue
            
            diff = target - nums[idx]
            
            if diff not in prev_seen:
                prev_seen[nums[idx]] = idx
            else:
                return [prev_seen[diff], idx]
                
    
    

if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([3,2,4], 6)
    
    print(result)
