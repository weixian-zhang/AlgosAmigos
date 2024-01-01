

class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
           
        
        max_no_house_1 = self._max_rob(nums[1:])
        max_no_house_2 = self._max_rob(nums[:-1])
                
        return max(max_no_house_1, max_no_house_2)
    
    def _max_rob(self, nums: list[int]) -> int:
        
        dp = [0 for x in nums]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
                       
            if i - 2 >= 0:                
                max_of_prev_houses = max(dp[:i-1])
                dp[i] += nums[i] + max_of_prev_houses
            else:
                dp[i] += max(nums[i], dp[i-1])
                
        return max(dp)
    
if __name__ == '__main__':
    
    s = Solution()
    
    r = s.rob([200,3,140,20,10])
    
    print(r)