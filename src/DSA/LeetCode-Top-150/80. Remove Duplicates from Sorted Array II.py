import sys
class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return 1
        
        dupTracker = {}
        i = 0
        
        while i <= len(nums) - 1 and nums[i] != sys.maxsize:
            
            currNum = nums[i]
            
            if currNum not in dupTracker:
                dupTracker[currNum] = 1
                i += 1
            elif currNum in dupTracker and dupTracker[currNum] != 2:
                dupTracker[currNum] += 1
                i += 1
            else:
                
                nums[i] = sys.maxsize
                
                temp = nums.pop(i)
                
                nums.append(temp)
            
        return sum(dupTracker.values())
            
    
    

if __name__ == '__main__':      
    s = Solution()
    print(s.removeDuplicates([1,1])) # [0,0,1,1,1,1,2,3,3]