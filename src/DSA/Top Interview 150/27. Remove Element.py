class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        numReplace = 10000
        
        x = 0
        while x <= len(nums) -1 :
            
            if nums[x] == val:
                
                nums[x] = numReplace
                
                removedVal = nums.pop(x)
                
                nums.append(removedVal)
                
                x -= 1
            else:
                x += 1
                
        nums.sort()
        
        k = 0
        i = len(nums)-1
        while i != -1 and nums[i] == numReplace:
            nums.pop(i)
            i -= 1
        
        return len(nums)
        
    
            
    

if __name__ == '__main__':
    s = Solution()
    r = s.removeElement([3,2,2,3],3)#([0,1,2,2,3,0,4,2], 2)
    print(r)