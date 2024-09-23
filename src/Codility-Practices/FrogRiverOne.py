# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(X, A):
    # Implement your solution here

    river = set([x for x in range(1, X + 1)])

    for k in range(len(A)):
        
        if A[k] in river:
            river.remove(A[k])
            
        if not river:
            return k
        
    return -1

print(solution(5, [3]))
print(solution(1, [1]))
print(solution(5, [1,3,1,4,2,3,5,4]))