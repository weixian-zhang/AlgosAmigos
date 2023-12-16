# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(A):
    # Implement your solution here
    
    A = set(A)

    counter = 1
    for x in range(len(A)):
        if counter not in A:
            return counter
        counter += 1

    return counter

print(solution([1, 3, 6, 4, 1, 2]))