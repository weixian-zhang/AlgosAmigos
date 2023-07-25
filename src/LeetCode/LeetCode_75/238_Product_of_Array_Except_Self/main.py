

class Solution:
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        
        length = len(nums)
        result = []
        left = [0] * length
        right = [0] * length
        
        for idx in range(length):
            if idx == 0:
                left[idx] = nums[idx]
            else:
                left[idx] = nums[idx] * left[idx-1]
        
        for idx in range(length-1, -1, -1):
            if idx == length-1:
                right[idx] = nums[idx]
            else:
                right[idx] = nums[idx] * right[idx+1]
        
        for idx in range(length):
            
            if idx == 0:
                result.append(right[1])
            elif idx == len(nums) - 1:
                result.append(left[idx-1])
            else:
                result.append(left[idx-1] * right[idx+1])
                
        return result
    

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([-1,1,0,-3,3]))