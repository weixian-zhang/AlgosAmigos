class Solution:
    
    def __init__(self) -> None:
        self.result = 0
        
    def calculate(self, s: str) -> int:
        
        result = 0
        sign = 1
        curr = 0
        stack = []
        
        for c in s:
            
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c in '-+':
                
                result += (sign * curr)
                
                if c == '-':
                    sign = -1
                else:
                    sign = 1
                    
                 # sign is to make curr number a negative or position. e.gL result += -4 ti handle minus(-)
                curr = 0
            
            if c == '(':
                stack.append(result)    # stack contains result, sign, result, sign depending on number of open/close parenthesis
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += (sign * curr)
                
                prev_sign = stack.pop()
                prev_result = stack.pop()
                
                result *= prev_sign
                
                result += prev_result * prev_sign
                
                curr = 0
        
        return result + (sign * curr)
            
            
    
                    
                    
            
            
        
        
    
if __name__ == '__main__':
    
    s = Solution()
    
    r = s.calculate('2-1 + 2') #(1+(4+5+2)-3)+(6+8)
    
    print(r)