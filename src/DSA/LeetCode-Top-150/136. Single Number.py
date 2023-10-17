class Solution:
    
    # with bit manipulation
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
    
    # without bit manipulation
    # def singleNumber(self, nums: list[int]) -> int:
          
    #     nums.sort()
        
    #     i, j =0, 1
        
    #     while i <= j and j <= len(nums)-1 and len(nums) > 1:
            
    #         if nums[i] == nums[j]:
    #             nums.pop(i)
    #             nums.pop(i)
    #         else:
    #             j += 1
    #             i += 1
                
    #     return nums[0]
                
      
      
      
if __name__ == '__main__':
    s = Solution()
    #s.singleNumber([2,2,1])
    #s.singleNumber([4,1,2,1,2])
    
    a = 0
    a = 235
    b = 134
    
    
    
    print(a^b)