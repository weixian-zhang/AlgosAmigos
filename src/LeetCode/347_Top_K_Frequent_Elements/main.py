class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        
        result = []
        freqList: dict = {}
        
        for n in nums:
            if n not in freqList:
                freqList[n] = 1
            else:
                freqList[n] += 1
                
        sortedDict = {num: freq for num,freq in sorted(freqList.items(), key=lambda item: item[1], reverse=True )}
        
        for x in range(0, k):
            result.append(list(sortedDict.keys())[x])
        
        return result
        

if __name__ == '__main__':
    
    nums =  [1,1,1,2,2,3]
    k = 2
    
    s = Solution()
    
    r = s.topKFrequent(nums, k)
    
    print(r)