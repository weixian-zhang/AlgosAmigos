# Smallest window in a String containing all characters of other String
# https://leetcode.com/problems/minimum-window-substring/

# my solution - Time Limit Exceeded
class Solution:

    def is_c_in_t(self, c: str, tMap: dict):
        
        if c in tMap:
            if tMap[c] > 0:
                tMap[c] = tMap[c] - 1
        else:
            return False, sum(list(tMap.values()))

        return True, sum(list(tMap.values()))

    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, deque

        if len(s) < len(t):
            return ''
        
        S = len(s)
        
        tMap = defaultdict(int)
        queue = deque([])

        for x in t:
            tMap[x] = tMap[x] + 1

        tMapCopy = tMap.copy()

        currMinSubstr = ''
        startIdx = -1

        # enqueue start points
        for idx, x in enumerate(s):
            if x in tMap:
                queue.append(idx)


        while queue:

            startIdx = queue.popleft()

            if (S-1) - startIdx < len(t) - 1:
                break

            idx = startIdx
            tMapCopy = tMap.copy()

            while idx <= S - 1:
                
                # mark section of c with start and end.
                # end means the section of c contains all chars of t
                # once hit end, record the substring
                isInT, leftoverMatchNum = self.is_c_in_t(s[idx], tMapCopy)

                if isInT and leftoverMatchNum == 0:
                    newSubstr = ''.join(s[startIdx: idx+1])
                    if not currMinSubstr:
                        currMinSubstr = newSubstr
                    elif len(newSubstr) < len(currMinSubstr):
                        currMinSubstr = newSubstr

                    break

                idx += 1

        return currMinSubstr


            
            

        


s = Solution()
print(s.minWindow("aaflslflsldkalskaaa", "aaa"))
print(s.minWindow('bdab', 'ab'))
print(s.minWindow('a', 'b'))
print(s.minWindow('a', 'aa'))
print(s.minWindow('ADOBECODEBANC', 'ABC'))
print(s.minWindow('this is a test string', 'tist'))