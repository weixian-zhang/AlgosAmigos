class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        # if not overlap interval found, return
        if len(intervals) == 0:
            return [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        # make a copy of interval to pop
        copiedInterval = intervals.copy()
        overlapIntervals = []
        
        i = 0
        while i <= len(copiedInterval) - 1:
            
            if self._is_overlap(copiedInterval[i], newInterval):
                overlapIntervals.append(copiedInterval[i])
                copiedInterval.pop(i)
            else:
                i += 1
            
    
        mergedInterval = newInterval
        
        if len(overlapIntervals) > 0:
    
            headMergedInterval = 0
            tailMergedInterval = 0
            
            # get head and tail of merge intervals
            headOfOverlapStart = overlapIntervals[0][0]
            newIntervalStart = newInterval[0]
            
            if newIntervalStart >= headOfOverlapStart:
                headMergedInterval = headOfOverlapStart
            else:
                headMergedInterval = newIntervalStart
                
            
            tailOfOverlapInterval = overlapIntervals[-1][1]
            newIntervalEnd = newInterval[1]
            
            if tailOfOverlapInterval >= newIntervalEnd:
                tailMergedInterval = tailOfOverlapInterval
            else:
                tailMergedInterval = newIntervalEnd
                
            
            mergedInterval = [headMergedInterval, tailMergedInterval]
            
            
        # insert the newly merged interval into original "head" and "tail"
        if len(copiedInterval) == 0:
            return [mergedInterval]
        

        for idx, i in enumerate(copiedInterval):
            if mergedInterval[0] < i[0]:
                copiedInterval.insert(idx, mergedInterval)
                break
                
        if mergedInterval[0] > copiedInterval[-1][0]:
            copiedInterval.append(mergedInterval)
            
                
        return copiedInterval
        
        
    def _is_overlap(self, a: list[int], b: list[int]):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        
        return (max(a1, b1) <= min(a2,b2))




s = Solution()
print(s.insert([[1,5]], [6,8]))
# print(s.insert([[1,5]], [2,3]))
# print(s.insert([[1,3],[6,9]],[2,5]))
# print(s.insert([[1,5]],[6,8]))
# print(s.insert([[1,5]],[2,3]))
# print(s.insert([], [5,7]))
# print(s.insert([[1,3],[6,9]], [2,5]))
# print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))