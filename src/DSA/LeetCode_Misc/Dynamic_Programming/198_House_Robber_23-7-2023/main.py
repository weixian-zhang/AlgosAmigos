

class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # stores max value of each house
        dp = [int(0) for x in range(len(nums))]
        
        #max money with 1 house
        dp[0] = nums[0]
        #max money for 2 houses
        dp[1] = max(nums[0], nums[1])
        
        #start at house 3 onwards
        for idx in range(2, len(nums)):
            
            prev_prev_house_max_money = dp[idx-2]
            
            # does current house + prev-prev house value is larger than the prev house
            maxVal = max( (nums[idx] + prev_prev_house_max_money), dp[idx - 1])
            
            dp[idx] = maxVal
        
        return dp[len(dp) - 1]
            
            
    

    # def robRecurse(self, nums, currentIdx, max):
        
        
    #     nextLeftHouseIdx = currentIdx - 2 if currentIdx - 1 != 0 and currentIdx - 2 >= 0 else -1
    #     nextRightHouseIdx = currentIdx + 2 if  currentIdx - 2 <= (len(nums) - 1) else -1
        
    #     if nextLeftHouseIdx == -1 and nextRightHouseIdx == -1:
    #         return max
        
    #     if nextLeftHouseIdx != -1 and nextRightHouseIdx != -1:
    #         max += max(nums[currentIdx] + nums[nextLeftHouseIdx], nums[currentIdx] + nums[nextRightHouseIdx])
    #         return self.robRecurse(nums, currentIdx + 1, max)
            
    #     elif nextLeftHouseIdx == -1 and nextRightHouseIdx != -1:
    #         max += nums[currentIdx]  + nums[nextRightHouseIdx]
    #         return self.robRecurse(nums, currentIdx + 1, max)
        
    #     elif nextLeftHouseIdx != -1 and nextRightHouseIdx == -1:
    #         max += nums[currentIdx] + nums[nextLeftHouseIdx]
    #         return self.robRecurse(nums, currentIdx + 1, max)
    
    
if __name__ == '__main__':
    
    s = Solution()
    maxVal = s.rob([2, 10, 3, 6, 8, 1, 7])
    
    print(maxVal)
