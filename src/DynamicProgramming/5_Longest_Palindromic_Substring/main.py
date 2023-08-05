class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        p_tracker = {}
        
        for i in range(len(s)):
            
            substr = s[:i+1]
            
            if self._is_palindrome(substr):
                p_tracker[len(substr)] = substr
            else:
                
                if len(substr) <= max(p_tracker):
                    continue
                
                # pop put chars one by one to test for palindrome
                substr_list = list(substr)
                
                curr_char = substr_list.pop(0)
                while curr_char != None:
                    
                    if len(substr_list) > 1 :
                        sub_sub_str = ''.join(substr_list)
                        if self._is_palindrome(sub_sub_str):
                            p_tracker[len(sub_sub_str)] = sub_sub_str
                        
                    if len(substr_list) > 1:
                        curr_char = substr_list.pop(0)
                        continue
                    
                    curr_char = None
                
                
        max_key = max(p_tracker)
        longest_palindrome =  p_tracker[max_key]
        return longest_palindrome
        
        
        
    def _is_palindrome(self, substr:str):
        
        if substr[::-1] == substr:
            return True
        return False
    

if __name__ == '__main__':
    
    s = Solution()
    
    r = s.longestPalindrome("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")
    
    print(r)
        
        