class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #self.rotate_right_with_extra_array_1(nums, k)
        
        self.rotate_right_with_extra_array_2(nums, k)
        # self.rotate_right_by_k_times(nums, k)
        
        # self.rotate_left_by_k_times(nums, k)
        
    def rotate_right_with_extra_array_1(self, nums, k):
        
        temp = [0 for x in nums]
        
        for x in range(len(nums)):
            
            idx = (x + k) % len(nums)
            temp[idx] = nums[x]
            
        for x in range(len(nums)):
            nums[x] = temp[x]
            
    def rotate_right_with_extra_array_2(self, nums: list[int], k):
        
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        
        left, right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        
        left, right = k, len(nums) -1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
            
        
        # if k > len(nums):
        #     k = len(nums)
        #     temp = nums.copy()
        # else:
        #     temp = nums[len(nums)-k: ]
        
        # lastIdx = len(nums)-1
        # for idx in range(len(nums)-k- 1, -1, -1):
        #     nums[lastIdx] = nums[idx]
        #     lastIdx -= 1
        
        # if temp != []:
        #     for x in range(k-1, -1, -1):
        #         nums[x] = temp[x]

        
        
    
    def rotate_right_by_k_times(self, nums: list[int], k: int):
        
        for x in range(k):
            
            temp = nums[len(nums) - 1]
            
            for idx in range(len(nums)-1, 0, -1):
                nums[idx] = nums[idx-1]
                
            nums[0] = temp
            
    def rotate_left_by_k_times(self, nums: list[int], k: int):
        
        for x in range(k):
            
            temp = nums[0]
            
            for idx in range(0, len(nums) - 1):
                nums[idx] = nums[idx + 1]
                
            nums[len(nums) - 1] = temp
        
        
if __name__ == '__main__':
    
    s = Solution()
    nums = [-1,-100,3,99] #[1,2] #[-1,-100,3,99], 2 #[1,2,3,4,5,6,7], 3
    s.rotate(nums, 2)
    print(nums)