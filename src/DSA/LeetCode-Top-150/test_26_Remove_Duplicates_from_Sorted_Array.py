class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        numTracker = []
        
        i = 0
        while i <= len(nums) - 1 and nums[i] != 10000:
            
            if nums[i] not in numTracker:
                numTracker.append(nums[i])
                i += 1
            else:
                num = nums[i]
                
                nums[i] = 10000
                
                temp = nums.pop(i)
                
                nums.append(temp)
                
                numTracker.remove(num)
                
                i -= 1
                
        k = 0
        
        # or just return the length of numTracker
        for x in nums:
            if x != 10000:
                k += 1
            else:
                break
            
        return k
    

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])