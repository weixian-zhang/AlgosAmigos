class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        
        result = 0
        for x in range(len(s)):
            
            j = 0
            while j <= len(g)-1:
                if g[j] <= s[x]:
                    result += 1
                    g.pop(j)
                    break
                else:
                    j += 1
                
        return result

    def binary_search(self, nums, target):
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            
            mid = high + low // 2
            
            if nums[mid] <= target:
                return mid
            else:
                high = mid - 1
                
        
        return -1
    
    
s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2,3], [1,2]))
print(s.findContentChildren([10,9,8,7], [10,9,8,7]))
