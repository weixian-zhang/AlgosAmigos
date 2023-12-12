# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    import math

    # Implement your solution here
    diff = Y - X

    return math.ceil((diff / D))

print(solution(10, 85, 30))

print(solution(50, 50000, 5))