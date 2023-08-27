

# DFS graph traversal
class DFS:
    
    def __init__(self) -> None:
        
        graph = {
            0, [()]
        }

class BFS:
    pass


# Dijkstra shortest path

# tree traversal
    # pre, in, post order
    
# binary search tree

# https://www.youtube.com/watch?v=us0cYQXQpxg
# permutations - of string with no repetition to get unique codes

class Permutation:
    
    def permute(self, strInput = 'abcde'):
        
        if not strInput:
            return []
        
        strings = [x for x in strInput]
        
        def _recurse(strings):
            
            if len(strings) == 0:
                return [[]]
            
            temp_perms = []
            
            first_char = strings[0]
            
            perms_without_first_char = _recurse(strings[1:])
            
            for permArr in perms_without_first_char:
                
                if len(permArr) == 0:
                    temp_perms.append([first_char])
                    break
                
                for idx in range(len(permArr)):
                    
                    first_part = permArr[0:idx]
                    
                    second_part = permArr[idx:]
                    
                    temp = first_part + [first_char] + second_part
                    
                    temp_perms.append(temp)
                
                
                first_char_at_back = permArr + [first_char]
                
                temp_perms.append(first_char_at_back)
                    
            
            return temp_perms
          
                    
        perms = _recurse(strings)         
            
        return perms


# https://www.youtube.com/watch?v=NA2Oj9xqaZQ
# combination - of string with no repetition to get unique codes

class Combinations:
    
    def gen_combo(self, strInput = 'abcd'):
        
        if not strInput:
            return [[]]
        
        result = []
        strings = [x for x in strInput]
        
        def _combos(strings):
            
            if len(strings) == 0:
                return [[]]
            
            first_char = strings[0]
            
            rest_of_chars = strings[1:]
            
            combos_without_first_char = _combos(rest_of_chars)
            
            combos_with_first_char = []
            
            for comboArr in combos_without_first_char:
                temp = comboArr + [first_char]
                combos_with_first_char.append(temp)
                
            return combos_without_first_char + combos_with_first_char
        
        combos = _combos(strings)
        return [x for x in combos if  len(x) > 0]

# merge sort

# quick sort




if __name__ == '__main__':
    
    # permutation = Permutation()
    # r = permutation.permute()
    # print(len(r))
    # print(r)
    
    combination = Combinations()
    combos = combination.gen_combo()
    print(len(combos))
    print(combos)