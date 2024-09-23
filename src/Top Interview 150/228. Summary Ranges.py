class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        
        if len(nums) == 0:
            return [""]
        
        if len(nums) == 1:
            return [f"{nums[0]}"]
        
        result = []
        left, right = 0, 1
        
        while left <= len(nums) - 1 and right <= len(nums) - 1:
            
            if nums[right] - 1 == nums[right-1]:
                right += 1  
            else:
                rightIdx = right-1
                if rightIdx == left:
                    result.append(f"{nums[left]}")
                else:
                    result.append(f"{nums[left]}->{nums[rightIdx]}")
                    
                left = right
                right += 1
        
        right -= 1  
               
        if right == left:
            result.append(f"{nums[left]}")
        else:
            result.append(f"{nums[left]}->{nums[right]}")
                        
                    
        return result
            
    

if __name__ == '__main__':
    
    s = Solution()
    
    # [0,1,2,4,5,7]
    # [0,2,3,4,6,8,9]
    
    print(s.summaryRanges([0,2,3,4,6,8,9]))