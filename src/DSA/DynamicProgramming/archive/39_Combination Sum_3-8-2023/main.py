class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        dp = [[] for x in range(target + 1)]
        
        for c in candidates:
            for t in range(target+1):
                
                if c > t: continue
                
                # case of single candidate = target
                if c == t:
                    dp[t].append([c])
                    
                for lis in dp[t-c]:
                    dp[t].append(lis + [c])
             
                
        
    


if __name__ == '__main__':
    s = Solution()
    
    s.combinationSum([2,3,6,7], 7)