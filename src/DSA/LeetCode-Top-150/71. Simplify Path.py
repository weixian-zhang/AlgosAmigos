class Solution:
    
    def simplifyPath(self, path: str) -> str:
        
        pathSegments = [x for x in path.split('/') if x != '' and x != '.']
        
        stack = []
        
        for x in pathSegments:
            if x == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(x)
                    
        return '/' + '/'.join(stack)
        
        
    # def simplifyPath(self, path: str) -> str:
        
    #     tempResult = [] # nested list of dirs
    #     fileDirName = ''
    #     separatorBuffer = []
        
    #     if path == '':
    #         return
    #     if path[0] == '/':
    #         path = path[1:]
    #     if path[-1] == '/':
    #         path = path[:-1]
        
    #     for x in range(0, len(path)):
            
    #         if self.is_valid_char(path[x]) and not separatorBuffer:
    #             fileDirName += path[x]
    #         elif self.is_valid_char(path[x]) and separatorBuffer:
    #             if self.is_single_dot(separatorBuffer) or self.is_double_slashes(separatorBuffer):
    #                 tempResult.append(fileDirName)
    #                 fileDirName = ''
    #                 fileDirName += path[x]
    #                 separatorBuffer = []
    #         elif not self.is_valid_char(path[x]):
    #             separatorBuffer.append(path[x])
                
    #             if self.is_double_dots(separatorBuffer):
    #                 tempResult = []
    #                 fileDirName = ''
    #                 separatorBuffer = []
                
    #     if fileDirName != '':
    #         tempResult.append(fileDirName)         
                 
    #     canonicalPath = ''
    #     canonicalPath += '/'.join(tempResult)
            
    #     return '/' + canonicalPath
                
    
    # def is_single_dot(self, separators):
    #     if ''.join(separators) == '/./':
    #         return True
    #     return False      
    
    # def is_double_dots(self, separators):
    #     separators = ''.join(separators)
    #     if separators == '/../' or separators == '../':
    #         return True
    #     return False   
    
    # def is_double_slashes(self, separators):
    #     if ''.join(separators) == '//':
    #         return True
    #     return False   
        
    # def is_valid_char(self, char: str):
        
    #     validChars = ['_', '...']
        
    #     if char.isalnum() or char in validChars:
    #         return True
        
    #     return False
    
    
if __name__ == '__main__':
    s = Solution()
    #s.simplifyPath('/home/../foo//bar')
    #s.simplifyPath('/home/')
    #s.simplifyPath('/a/./b/../../c/')
    #s.simplifyPath("/a//b////c/d//././/..")
    s.simplifyPath("/../")