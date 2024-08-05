class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y:  int(x / y)
        }

        for x in tokens:

            if x.lstrip('-').isdigit():
                stack.append(int(x))
                continue
            
            rightOperand = stack.pop()
            leftOperand = stack.pop()
            r = operators[x](leftOperand, rightOperand)
            stack.append(r)

        return stack.pop()


s = Solution()
#print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))