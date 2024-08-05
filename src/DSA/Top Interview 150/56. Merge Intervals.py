class Solution:
                      
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return [intervals[0]]
        
        tempResult = []
        
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
    
            
    def _merge(self, a, b):
        
        minStart = min(a[0], b[0])
        maxStart = max(a[1], b[1])
        return [minStart, maxStart]
        
    def isoverlap(self, a, b):
        aStart, aEnd = a[0], a[-1]
        bStart, bEnd = b[0], b[-1]
        
        if bStart <= aEnd: #:aStart <= bEnd and bStart <= aEnd:
            return True
        
        return False

                
    
    
if __name__ == '__main__':
    s = Solution()
    
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[1,3]], [[1,4],[0,4]], [[1,4],[2,3]], [[2,3],[4,5],[6,7],[8,9],[1,10]]