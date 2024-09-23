from typing import List

class Solution:

    # 4 months ago solution - Sep 2023
    # def rotate(self, nums: list[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        
    #     #self.rotate_right_with_extra_array_1(nums, k)
        
    #     self.rotate_right_with_extra_array_2(nums, k)
    #     # self.rotate_right_by_k_times(nums, k)
        
    #     # self.rotate_left_by_k_times(nums, k)
        
    # def rotate_right_with_extra_array_1(self, nums, k):
        
    #     temp = [0 for x in nums]
        
    #     for x in range(len(nums)):
            
    #         idx = (x + k) % len(nums)
    #         temp[idx] = nums[x]
            
    #     for x in range(len(nums)):
    #         nums[x] = temp[x]
            
    # def rotate_right_with_extra_array_2(self, nums: list[int], k):
        
    #     k = k % len(nums)
        
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -=1
        
    #     left, right = 0, k-1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -=1
        
    #     left, right = k, len(nums) -1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -=1
            
        
    #     # if k > len(nums):
    #     #     k = len(nums)
    #     #     temp = nums.copy()
    #     # else:
    #     #     temp = nums[len(nums)-k: ]
        
    #     # lastIdx = len(nums)-1
    #     # for idx in range(len(nums)-k- 1, -1, -1):
    #     #     nums[lastIdx] = nums[idx]
    #     #     lastIdx -= 1
        
    #     # if temp != []:
    #     #     for x in range(k-1, -1, -1):
    #     #         nums[x] = temp[x]

        
        
    
    # def rotate_right_by_k_times(self, nums: list[int], k: int):
        
    #     for x in range(k):
            
    #         temp = nums[len(nums) - 1]
            
    #         for idx in range(len(nums)-1, 0, -1):
    #             nums[idx] = nums[idx-1]
                
    #         nums[0] = temp
            
    # def rotate_left_by_k_times(self, nums: list[int], k: int):
        
    #     for x in range(k):
            
    #         temp = nums[0]
            
    #         for idx in range(0, len(nums) - 1):
    #             nums[idx] = nums[idx + 1]
                
    #         nums[len(nums) - 1] = temp


    # brute force - time limit exceed
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        
    #     if len(nums) == 1:
    #         return nums
        
    #     lastEle = nums[-1]
    #     first = nums[0]

    #     for _ in range(k):
    #         for x in range(len(nums) - 2, -1, -1):
    #             nums[x + 1] = nums[x]

    #         nums[0] = lastEle

    #         lastEle = nums[-1]
        
    #     return nums
    
    # refresher Jan 2024
    # extra space
    def rotate(self, nums: List[int], k: int) -> None:

        numsList = nums.copy()

        x = 1
        while x <= k:
            n = numsList.pop()
            numsList = [n] + numsList
            x += 1

        for x in range(len(numsList)):
            nums[x] = numsList[x]

        
        
        
if __name__ == '__main__':
    
    s = Solution()
    nums = [-1,-100,3,99] #[1,2] #[-1,-100,3,99], 2 #[1,2,3,4,5,6,7], 3
    print(s.rotate([1,2,3,4,5,6,7], 3))
    # print(s.rotate([-1,-100,3,99], 2))
    