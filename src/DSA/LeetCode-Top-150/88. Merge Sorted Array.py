class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = 0, 0
        
        # merge nums2 into nums1 by replace 0s of nums1 with nums2 numbers
        
        while i <= (len(nums1) - 1) and j <= (len(nums2) - 1):
            
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
                i += 1
            else:
                i += 1
                
        self._quicksort(nums1)
                
    
    def _quicksort(self, nums):
        
        
        def _recurse(nums, start, end):
            
            pivotIdx = end
            i, j = start - 1, start
            
            while j <= end:
                if nums[j] > nums[pivotIdx]:
                     i += 1
                     j += 1
                     _swap(nums, i, j)
                else:
                    j += 1
                     
            # swap pivotIdx with i, somehwree in the middle after this algorithm
            i += 1
            _swap(nums, i, pivotIdx)
            
            # sort left
            _recurse(nums, 0, pivotIdx)
            
            # sort right
            _recurse(nums, pivotIdx + 1, len(nums) - 1)
                     
        def _swap(nums, src, dest):
            
            temp = nums[src]
            nums[src] = nums[dest]
            nums[dest] = temp
            
        
        _recurse(nums, 0 , len(nums) - 1)
        
        
if __name__ == '__main__':
    
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    r = s.merge(nums1,3,  [2,5,6],3)
    print(nums1)
        