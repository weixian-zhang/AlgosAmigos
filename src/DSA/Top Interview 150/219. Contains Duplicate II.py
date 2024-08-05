class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        visited= {}
        
        for x in range(len(nums)):
            if nums[x] not in visited:
                visited[nums[x]] = [x]
            else:
                visited[nums[x]].append(x)
        
        
        for indexes in visited.values():
            for x in range(len(indexes)-1):
                if abs(indexes[x] - indexes[x+1]) <= k:
                    return True
                
        return False
    
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1], 3))
    print(s.containsNearbyDuplicate([1,0,1,1],1))
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))