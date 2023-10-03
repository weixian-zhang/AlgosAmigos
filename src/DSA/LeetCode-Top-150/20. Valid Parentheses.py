class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []
        stackClosed = []
        allParentheses = {'{': '}', '[':']', '(' : ')' }
        allCloseP = ['}', ']', ')' ]
        
        for c in s:
            stack.append(c)
            
        p = self.try_pop(stack)
        
        while p is not None:
            
            if p in allCloseP:
                stackClosed.append(p)
            else:
                tempClosed = self.try_pop(stackClosed)
                if allParentheses[p] != tempClosed:
                    return False
            
            p = self.try_pop(stack)
                
        if len(stackClosed) > 0:
            return False  
        
        return True
    
    def try_pop(self, stack):
        try:
            temp = stack.pop() 
            return temp
        except:
            return None
            
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("))")) #"(]")) , "()[]{}")), "{[]}"