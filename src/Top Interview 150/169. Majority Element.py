class Solution:
    def majorityElement(self, nums: list[int]) -> int:
            
        if len(nums) == 1:
            return nums[0]
        if nums == []:
            return 0
        
        nums.sort()
        midIdx = len(nums) // 2
        
        return nums[midIdx]
            

if __name__ == '__main__':      
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))
