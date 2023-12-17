# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(A):
    # Implement your solution here
    A = [abs(x) for x in A]
    A = set(A)
    return len(A)

print(solution([-5, 5]))
print(solution([-5]))
print(solution([-5,-3,-1,0,3,6]))