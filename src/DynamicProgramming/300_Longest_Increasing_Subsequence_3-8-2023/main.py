
# [10,9,2,5,3,7,101,18]

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        dp = [1 for x in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
        # 1+ is for last number
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    
    r = s.lengthOfLIS([1,3,6,7,9,4,10,5,6])  #[10,9,2,5,3,7,101,18])
    print(r)
    
            
            