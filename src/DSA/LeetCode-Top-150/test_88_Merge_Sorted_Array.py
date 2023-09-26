class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = m, 0
        
        while i <= (len(nums1) - 1) and j <= (len(nums2) - 1):
            
            if nums1[i] == 0:

                nums1[i] = nums2[j]
                
                for x in range(i, 0, -1):
                    if nums1[x] < nums1[x-1]:
                        nums1[x], nums1[x-1], = nums1[x-1], nums1[x]
                    else:
                        break
                        
                j += 1
                i += 1
            else:
                i += 1
        
                
    
    def _quicksort(self, nums):
        
        
        def _recurse(nums, start, end):
            
            if start >= end:
                return
            
            pivotIdx = end
            i = start - 1
            
            for j in range(start, end):
                if nums[j] < nums[pivotIdx]:
                    i += 1
                    _swap(nums, i, j)
                    
            
            # swap pivotIdx with i, somehwree in the middle after this algorithm
            i += 1
            _swap(nums, i, pivotIdx)
            
            # i is the new pivot
            
            # sort left
            _recurse(nums, 0, i - 1)
            
            # sort right
            _recurse(nums, i + 1, end)
                     
        def _swap(nums, src, dest):
            
            temp = nums[src]
            nums[src] = nums[dest]
            nums[dest] = temp
            
        
        _recurse(nums, 0 , len(nums) - 1)


import pytest

class TestSolution:
    # @pytest.mark.parametrize('nums1,m,nums2,n', [
    #     ([4,5,6,0,0,0],3,[1,2,3],3),
    #     ([2,0],1,[1],1),
    #     ([1,2,3,0,0,0],3,[2,5,6],3),
    #     ([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
    # ])
    # def test_merge_sorted_array(nums1, m, nums2, n):
    #     s = Solution()
    #     r = s.merge(nums1,m,nums2,n)
        
    def test_merge_sorted_array_1(self, nums1=[-1,0,0,3,3,3,0,0,0],m=6,nums2=[1,2,2], n=3):
         s = Solution()
         s.merge(nums1,m,nums2,n)
         assert nums1 == [-1,0,0,1,2,2,3,3,3]
         
    def test_merge_sorted_array_2(self, nums1=[2,0],m=1,nums2=[1], n=1):
         s = Solution()
         s.merge(nums1,m,nums2,n)
         assert nums1 == [1,2]
         
    def test_merge_sorted_array_3(self, nums1=[4,5,6,0,0,0],m=3,nums2=[1,2,3], n=3):
         s = Solution()
         s.merge(nums1,m,nums2,n)
         assert nums1 == [1,2,3,4,5,6]
        
if __name__ == '__main__':
    
    s = Solution()
    
    r = s.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2], 3)
    
        