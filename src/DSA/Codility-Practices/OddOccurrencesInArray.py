# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 66%
# 80% correctness, 50% performance
# def solution(A):
#     # Implement your solution here
#     unqNums= list(set(A))
#     numTracker = {}
#     for x in unqNums:
#         numTracker[x] = False

#     A.sort()
#     for a in A:
#         numTracker[a] += 1
    
#     for k, v in numTracker.items():
#         if v == 1:
#             return k

# 100%
def solution(A):
    
    # Implement your solution here
    if len(A) == 1:
        return A[0]

    unqNums = list(set(A))
    
    A.sort()
    
    anchor, forward = 0, 1

    while forward <= len(A) - 1:

        if A[anchor] == A[forward]:
            anchor = forward + 1
            forward = anchor + 1
            continue

        forward += 1

    return A[anchor]
    
    
            
print(solution([9,6,3,9,3,3,7,3,7,7,9]))
print(solution([9,3,9,3,3,7,3,7,7,6,9]))
print(solution([9,3,9,3,9,7,9]))
