from typing import List
from collections import deque
from functools import lru_cache

class Solution:

    # BFS
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        q = deque([0])  # start at 0 index of s
        ws = set(wordDict)
        seen = set()
        

        while q:
            
            startIdx = q.popleft()

            if startIdx == len(s):
                return True

            for endIdx in range(startIdx + 1, len(s) + 1):
                if endIdx in seen:
                    continue
                
                if s[startIdx:endIdx] in ws:
                    q.append(endIdx)
                    seen.add(endIdx)


        return False
    
    # recursion + manual dict for memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        S = len(s)
        dp = {}

        allWordFound = False

        def dfs(currIdx: int):
            nonlocal allWordFound

            if currIdx >= S:
                return True
            
            if currIdx in dp:
                  return dp[currIdx]

            for w in wordDict:
                if s[currIdx:currIdx + len(w)] == w:
                    allWordFound = dfs(currIdx + len(w))
                    dp[currIdx] = allWordFound

                    if allWordFound:
                        return True
                    #print(f'{currIdx}: {allWordFound}')

            dp[currIdx] = False
            return False
                
        result = dfs(0)

        return result
    

    # recursion + memoization - more elegant way of writing
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache
        def dfs(currIdx: int):

            if currIdx >= len(s):
                return True
    
            for w in wordDict:
                if s[currIdx:currIdx + len(w)] == w and dfs(currIdx + len(w)):
                    return True
            else:
                return False
                
        return dfs(0)
    

    # dp bottom up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        S = len(s) - 1
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for x in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (x + len(w)) <= len(s) and s[x: x + len(w)] == w:
                    dp[x] = dp[x + len(w)]
            
                if dp[x]:
                    break

        return dp[0]
                    
                



    
s = Solution()
print(s.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))
print(s.wordBreak('cars', ["car","ca","rs"]))
# print(s.wordBreak('a', ["b"]))
print(s.wordBreak('leetcode', ["leet","code"]))
# print(s.wordBreak('applepenapple', ["pen","apple"]))
print(s.wordBreak('catsandog', ["cats","dog","sand","and","cat"]))
# print(s.wordBreak('aaaaaaa', ["aaaa","aaa"]))
#print(s.wordBreak('dadasdbcapokoqp', ["bca"]))