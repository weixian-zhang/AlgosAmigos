class Solution:
    
    # 2 pointers is more space efficient
    # space complexity = O(1)
    # time complexity = O(n) due to cleansing string to alphanum one by one thru N
    def isPalindrome(self, s: str) -> bool:
        
        cleansedStr = [x.lower() for x in s if x.isalnum() and x != '']
        cleansedStr = ''.join(cleansedStr)
        
        def _is_palindrome(chars: str):
            
            mid = len(chars) // 2
            
            i,j = mid, mid
            if len(chars) % 2 == 0:
                i, j = mid-1, mid
            
            while i >= 0 and j <= len(chars)-1:
                
                if chars[i] != chars[j]:
                    return False
                
                i -= 1
                j += 1
            
            return True
        
        return _is_palindrome(cleansedStr)
                
                
        
        
    # reverse string solution
    # def isPalindrome(self, s: str) -> bool:
        
    #     cleansedStr = [x.lower() for x in s if x.isalnum() and x != '']
    #     cleansedStr = ''.join(cleansedStr)
    #     reverseStr = cleansedStr[::-1]
    #     return cleansedStr == reverseStr


if __name__ == '__main__':
    
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
    #print(s.isPalindrome('0P'))