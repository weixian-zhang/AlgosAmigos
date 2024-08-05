from typing import List

class Solution:

    # neetcode explained solution
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def _backtracking(open: int, close: int, strBuilder: list):
            
            if len(strBuilder) == n * 2:
                result.append(''.join(strBuilder))
                return
            
            if open < n:
                strBuilder += '('
                _backtracking(open + 1, close, strBuilder)
                strBuilder.pop()

            if close < open:
                strBuilder += ')'
                _backtracking(open, close + 1, strBuilder)  
                strBuilder.pop()
                      

        _backtracking(0, 0, [])
                
        return result


s = Solution()
print(s.generateParenthesis(3))