# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
# use stack to track open brack
def solution(S):
    # Implement your solution here

    if not S:
        return 1
    
    open_brackets = []

    for c in S:
        if c == '(':
            open_brackets.append('(')
        else:
            if not open_brackets:
                return 0
            
            ob = open_brackets.pop()
            if ob + c != '()':
                return 0
            
    return 1 if not open_brackets else 0

print(solution(')('))
# print(solution('((((()))))'))
# print(solution('((((('))
# print(solution(''))
# print(solution('(()(())())')) # 1
# print(solution('())')) # 0