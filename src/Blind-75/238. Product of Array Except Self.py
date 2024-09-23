from typing import List

class Solution:

    # division method
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Calculate the total product of non-zero elements and count zeros
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        result = []
        for num in nums:
            if zero_count == 0:
                # No zeros in the array, normal division
                result.append(total_product // num)
            elif zero_count == 1:
                # One zero in the array
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                # More than one zero in the array
                result.append(0)

        return result
    
    # get right product first
    # get left product
    # multiply both left and right to "combine" and get product of both ways
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        prefixLeft, suffixRight = [1] * N, [1] * N

        for i in range(1, N):
            prefixLeft[i] = prefixLeft[i - 1] * nums[i - 1]

        for i in range(N-2, -1, -1):
            suffixRight[i] = suffixRight[i + 1] * nums[i + 1]

        return [l*r for l,r in zip(prefixLeft, suffixRight)]
    

    # greg hogg solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_multi, r_multi = 1, 1
        n = len(nums)
        l_arr, r_arr = [1] * n, [1] * n

        for i in range(n):
            j = -i - 1 # j iterate from back to front: -1, -2, -3, ...
            
            l_arr[i] = l_multi  # set previous multiply result to prefix 
            r_arr[j] = r_multi  # set previous multiply result to suffix 

            l_multi *= nums[i] # stores previous value of multiply
            r_multi *= nums[j] # stores previous value of multiply

        return [l*r for l,r in zip(l_arr, r_arr)]


s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3,0,1]))