class Solution:
    
    # eval outwards using "2 pointers"
    def longestPalindrome(self, s: str) -> str:
        
        
        result = ''
        result_len = 0
        
        left = 0
        right = 0
        
        for i in range(len(s)):
            left, right = i,i
            
            # eval odd length substr e.g racecar
            while left >= 0 and right < len(s) and s[left] == s[right] :
                
                curr_substr_len = (right - left) + 1
                
                if curr_substr_len > result_len:
                    result = s[left:right+1]
                    result_len = curr_substr_len
                
                left -= 1
                right +=1 
                
            # eval even length substr e.g abba
            
            left, right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right] :
            
                curr_substr_ken = (right - left) + 1
                
                if curr_substr_ken > result_len:
                    result = s[left:right+1]
                    result_len = curr_substr_ken
                
                left -= 1
                right +=1 
                
        
        return result
    
    # def longestPalindrome(self, s: str) -> str:
        
    #     result = ''
        
    #     dp = [0 for c in s]
    #     for idx in range(len(s)):
    #         dp[idx] = [0 for c in s]
        
    #     for i in range(len(s)):
    #             j = 0
    #             if i == 1:
    #                 j = 1
    #             elif i > 1:
    #                 j = i
    #             dp[i][j] = 1
    
    #     for i in range(len(s)):
    #         for j in range(len(s)):
                
    #             if s[i] == s[j]:
                    
    #                 temp_i = i
    #                 temp_j = j
                    
                    
                    
    #                 while (temp_j >= temp_i) and s[temp_i] == s[temp_j]:
    #                     substr = s[temp_i:temp_j+1]
    #                     if len(substr) > len(result) and substr == self._reverse_str(substr):
    #                         result = substr
                            
    #                     dp[temp_i][temp_j] += 1 + dp[temp_i][temp_j-1]
                        
    #                     temp_i += 1
    #                     temp_j -= 1
                    
    #                 #if (temp_j - temp_i)+1 > len(result):
                        
    #             else:
    #                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                        
                        
                
    #     print(result)
        
    # def _reverse_str(self, s):
    #     return s[::-1]

            
        

    
    # brute force O(N3)
    # def longestPalindrome(self, s: str) -> str:
        
    #     p_tracker = {}
        
    #     for i in range(len(s)):
            
    #         substr = s[:i+1]
            
    #         if self._is_palindrome(substr):
    #             p_tracker[len(substr)] = substr
    #         else:
                
    #             if len(substr) <= max(p_tracker):
    #                 continue
                
    #             # pop put chars one by one to test for palindrome
    #             substr_list = list(substr)
                
    #             curr_char = substr_list.pop(0)
    #             while curr_char != None:
                    
    #                 if len(substr_list) > 1 :
    #                     sub_sub_str = ''.join(substr_list)
    #                     if self._is_palindrome(sub_sub_str):
    #                         p_tracker[len(sub_sub_str)] = sub_sub_str
                        
    #                 if len(substr_list) > 1:
    #                     curr_char = substr_list.pop(0)
    #                     continue
                    
    #                 curr_char = None
                
                
    #     max_key = max(p_tracker)
    #     longest_palindrome =  p_tracker[max_key]
    #     return longest_palindrome
        
        
        
    # def _is_palindrome(self, substr:str):
        
    #     if substr[::-1] == substr:
    #         return True
    #     return False
    

if __name__ == '__main__':
    
    s = Solution()
    
    r = s.longestPalindrome('aaabbaa') #"aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")
    
    print(r)
        
        