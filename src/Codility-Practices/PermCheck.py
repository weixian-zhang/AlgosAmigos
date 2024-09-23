# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(A):
    # Implement your solution here

    
    perms = set([x for x in range(1, len(A) + 1)])
    A = list(set(A))

    for x in range(len(A)):
        if A[x] in perms:
            perms.remove(A[x])
        
    return 1 if not perms else 0

print(solution([1, 1]))
print(solution([2]))
print(solution([10,5,9,3,1,1,1,4,8,3,2]))
print(solution([4,1,3,2]))
print(solution([4,1,3]))