class Solution:

    
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0
        if len(s) == 1:
            return 1

        S = len(s) - 1
        
        curr_substr = [s[0]]
        result = len(curr_substr)

        left, right = 0, 1


        while left <= right and right <= S:

            if s[right] not in curr_substr:
                curr_substr.append(s[right])
                result = max(result, len(s[left:right + 1]))
                right += 1
                continue
            
            # found a repeat char
            while s[right] in curr_substr:
                 #temp = list(curr_substr)
                 curr_substr.pop(0)
                 #curr_substr = set(temp)
                 left += 1
                
                

        return result


        