class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        temp = [x for x in nums1 if x != 0] + [x for x in nums2 if x != 0]
        nums1 = temp
        nums1.sort()
        
        
if __name__ == '__main__':
    
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    r = s.merge(nums1,3,  [2,5,6],3)
    print(nums1)
        