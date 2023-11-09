class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        citations.sort()
        hIndex= 0

        for x in range(len(citations)):

            if citations[x] == 0:
                continue

            atLeast = citations[x]

            p = x + 1
            paperCount = 1
            while p <= len(citations) - 1:
                paperCount += 1
                p += 1

            if atLeast <= paperCount:
                hIndex = max(hIndex, atLeast)
            else:
                hIndex = max(hIndex, paperCount)

        return hIndex


s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([100]))
