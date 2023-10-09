import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        minSubArrLen = sys.maxsize
        curr_sum = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            
            curr_sum += nums[window_end]
            
            while curr_sum >= target:
                minSubArrLen = min(minSubArrLen, window_end+1 - window_start)
                curr_sum -= nums[window_start]
                window_start += 1
                
                  
        if  minSubArrLen == sys.maxsize:    
            minSubArrLen = 0
            
        return minSubArrLen
                    
    

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
    #print(s.minSubArrayLen(4, [1,4,4]))
    #print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))