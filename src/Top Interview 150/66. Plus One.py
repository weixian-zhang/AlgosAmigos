class Solution:
    
    # better solution is to add 1 number at a time and record "carry over" number
    def plusOne(self, digits: list[int]) -> list[int]:
        
        carry = 0
        result = []
        pointer = len(digits) - 1
        
        while pointer >= 0:
            
            if pointer == len(digits) - 1:
                if digits[pointer] + 1 == 10:
                    carry += 1
                    result.insert(0, 0)     # insert num at the "front"
                else:
                    result.insert(0, digits[pointer] + 1)  
            else:
                if carry == 1:
                    if digits[pointer] + 1 == 10:
                        result.insert(0, 0)
                    else:
                        carry = 0
                        result.insert(0, digits[pointer] + 1)  
                
                else:
                    if carry != 0:
                        carry = 0
                    result.insert(0, digits[pointer])  
                    
            pointer -= 1
            
        if carry == 1:
            result.insert(0, 1)
            carry = 0 
            
        return result
                
    
    # my solution convert to str then to int to add one and convert back -> int -> list
    # def plusOne(self, digits: list[int]) -> list[int]:
        
    #     oneDigit = int(''.join([str(x) for x in digits])) + 1
        
    #     result = [int(x) for x in str(oneDigit)]
        
    #     return result
        
    

s = Solution()
print(s.plusOne([9,9,9,9]))
# print(s.plusOne([9]))
# print(s.plusOne([1,2,3]))
# print(s.plusOne([4,3,2,1]))
    