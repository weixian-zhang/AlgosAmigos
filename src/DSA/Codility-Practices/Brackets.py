# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(S):
    # Implement your solution here
    bracketMap = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    openBrackets = ['(', '{', '[']
    stack = []

    for c in S:
        if c in openBrackets:
            stack.append(c)
        else:
            if not stack:
                return 0
            openBracket = stack.pop()
            if bracketMap[c] != openBracket:
                return 0
            
    return 1 if not stack else 0

print(solution('{{{{'))
print(solution(')('))
print(solution('{[()()]}'))
print(solution('([)()]'))