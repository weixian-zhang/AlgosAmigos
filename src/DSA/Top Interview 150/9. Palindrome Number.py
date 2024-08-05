class Solution:
    
    # 2 pointers compare from mid both side outwards
    def isPalindrome(self, x: int) -> bool:
        
        xStr = str(x)
        
        mid = (len(xStr)-1) // 2
        
        left, right = mid, mid
        
        if len(xStr) % 2 == 0:
            right = mid + 1
            
        while left >= 0 and right <= len(xStr) - 1:
            
            if xStr[left] != xStr[right]:
                return False
            
            left -= 1
            right += 1
            
        return True
        
    
    # reverse string solution
    # def isPalindrome(self, x: int) -> bool:
        
    #     xStr = str(x)
        
    #     xStrReverse = xStr[::-1]
        
    #     return xStr == xStrReverse
    
    
    
if __name__ == '__main__':
    s = Solution()
    #print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))