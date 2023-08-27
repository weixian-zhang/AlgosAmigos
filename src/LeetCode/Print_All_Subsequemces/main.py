

# https://www.youtube.com/watch?v=NA2Oj9xqaZQ

class Solution:
    
    def combinations(self, elements, result):
    
        if len(elements) == 0:
            return [[]]
        
        first_char = elements[0]
        
        rest_of_chars = elements[1:]
        
        combos_without_first = self.combinations(rest_of_chars, result)
        
        combos_with_first = []
        
        for combo in combos_without_first:
            new_combo = combo + [first_char]
            combos_with_first.append(new_combo)
        
        return combos_with_first + combos_without_first
        
        
        


if __name__ == '__main__':
    
    s = Solution()
    
    print(s.combinations(['a','b','c'], []))