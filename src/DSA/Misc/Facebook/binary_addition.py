
# def add(binA: str, binB: str):

#     binA = binA.lstrip('0')
#     binB = binB.lstrip('0')
#     result = []

#     def prepend(s: str):
#         nonlocal result
#         result.insert(0, s)
    
#     i, j = len(binA) - 1, len(binB) - 1
    
#     carry = 0

#     while i >= 0 or j >= 0:

#         digitA = int(binA[i]) if i >= 0 else 0
#         digitB = int(binB[j]) if j >= 0 else 0

#         total = digitA + digitB + carry

#         brChar = str(total % 2)

#         prepend(brChar)

#         carry = total // 2

#         i -= 1
#         j -= 1


#     if carry == 1:
#         prepend('1')

#     return ''.join(result)

class Solution:
    def answer(self, binA: str, binB: str) -> int:
        pass



    
s = Solution()
print(s.answer('111000111000', '111011111111'))
print(s.answer('10101010', '11001100'))

    


# print(add('111000111000', '111011111111'))
# print(add('10101010', '11001100'))
# print(add('1010', '11'))
# print(add('1111', '111'))
# print(add('100101', '10101'))