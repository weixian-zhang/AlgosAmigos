class Solution:

    # def _calc(self, nums: list[str]):
    #     curr, result = 0, 0
    #     sign = 1

    #     for char in nums:
    #         if char.isdigit():
    #             curr = curr * 10 + int(char)
    #         else:
    #             result += sign * curr
    #             sign = 1 if char == '+' else -1
    #             curr = 0 
        
    #     return result + (sign * curr)

    # def calculate(self, s: str) -> int:
    #     if len(s) == 1:
    #         if s.isdigit():
    #             return int(s)
    #         return 0
        
    #     stack = []
    #     normalizedStack = []

    #     for c in s:
    #         if c == ' ':
    #             continue
    #         stack.append(c)

    #     result = 0

    #     while stack:

    #         curr = stack.pop()
            
    #         if curr == ')':
                
    #             count = 1
    #             tempStack = []

    #             while count != 0:

    #                 curr = stack.pop()

    #                 if curr == ')':
    #                     count += 1
    #                     continue

    #                 if curr == '(' and count != 0:
    #                     count -= 1
    #                     continue

    #                 tempStack = [curr] + tempStack

    #             temp_result = self._calc(tempStack)

    #             normalizedStack = [str(temp_result)] + normalizedStack

    #         if curr.isdigit() or curr in ['-', '+']:
    #             normalizedStack = [curr] + normalizedStack
    #             continue

    #     result = self._calc(normalizedStack)

    #     return result

    def calculate(self, s: str) -> int:
        
        curr, result = 0, 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char in ['+', '-']:
                result += sign * curr

                sign = 1 if char == '+' else -1

                curr = 0
            
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * curr

                result *= stack.pop()

                result += stack.pop()

                curr = 0

        r = result + (sign * curr)

        return r
            


s = Solution()
print(s.calculate("1-(     -2)"))
#print(s.calculate("222222 - 333333"))
#print(s.calculate("2147483647"))
# print(s.calculate("(1)"))
# print(s.calculate("1 + 1"))
# print(s.calculate("2-1 + 2"))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))