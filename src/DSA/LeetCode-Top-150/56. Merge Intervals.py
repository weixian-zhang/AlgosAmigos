class Solution:
    
    # def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
    #     mergeResult = []
    #     minStart = min([x[0] for x in intervals])
    #     maxEnd = max([x[1] for x in intervals])
        
    #     intervalTable = [-1 for x in range(minStart, maxEnd+1)]
        
    #     for x in intervals:
    #         startIdx = x[0] - 1
    #         endIdx = x[1]
            
    #         for j in range(startIdx, endIdx):
    #             intervalTable[j] =  1
        
    #     mergeSlices = []
    #     i, j = 0, 0
        
    #     while i <= len(intervalTable)-1 and j <= len(intervalTable)-1:
            
            
    #         if intervalTable[j] == 1:
    #             j += 1
    #         elif intervalTable[j] == -1 and j > i:
    #             mergeSlices.append([i+1, j])
    #             j += 1
    #             i = j
    #         else:
    #             i += 1
    #             j += 1
                
    #     if i < j:
    #         mergeSlices.append([i+1, j])
            
        
    #     return mergeSlices
            
            
        
            
        
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return [intervals[0]]
        
        result = []
        tempMerger = []
        tempResult = []
        overlapIdx = 0
        
        import operator
        intervals.sort(key=operator.itemgetter(0))
        
        merged = []
        
        for idx in range(0, len(intervals)):
            
           if merged == []:
               merged = intervals[idx]
           else:
               if self.isoverlap(merged, intervals[idx]):
                   merged = self._merge(merged, intervals[idx])
                   
                   if idx == len(intervals) - 1:
                       tempResult.append(merged)
                       
               else:
                   tempResult.append(merged)
                   merged = intervals[idx]
                   
                   if idx == len(intervals) - 1:
                       tempResult.append(intervals[idx])
                       
        
        return tempResult      
    
        
        # for x in tempResult:
            
        #     minStart = min([i[0] for i in x])  
        #     maxEnd = max([i[1] for i in x])  
            
        #     result.append([minStart, maxEnd])
            
        # return result
            
    
    def _merge(self, a, b):
        
        minStart = min(a[0], b[0])
        maxStart = max(a[1], b[1])
        return [minStart, maxStart]
        
    def isoverlap(self, a, b):
        aStart, aEnd = a[0], a[-1]
        bStart, bEnd = b[0], b[-1]
        
        if aStart <= bEnd and bStart <= aEnd:
            return True
        
        return False

                
    
    
if __name__ == '__main__':
    s = Solution()
    
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[1,3]], [[1,4],[0,4]], [[1,4],[2,3]], [[2,3],[4,5],[6,7],[8,9],[1,10]]