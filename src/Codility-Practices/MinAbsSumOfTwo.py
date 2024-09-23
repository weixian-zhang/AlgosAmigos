# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# brute force method - O(N2)
# 36% total
# 100# correctness
# 0# performance
def solution(A):
    import sys
    # Implement your solution here

    if not A:
        return 0
    
    minSum = sys.maxsize

    for i in range(len(A)):
        for j in range(len(A)):
            minSum= min(minSum, abs(A[i] + A[j]))

    return minSum if minSum != sys.maxsize else abs(A[0])

# 2 pointers solution, more efficient O(N)
# 63%
# 100% correctness
# 42% performance
def solution(A):
    import sys

    if not A:
        return 0
    
    A.sort()
    minSum = sys.maxsize

    left, right = 0, len(A) - 1

    while left < right:

        minSum = min(minSum, abs(A[left] + A[right]))

        if abs(A[left]) > abs(A[right]):
            left += 1
        else:
            right -= 1

    for x in A:
        minSum = min(minSum, abs(x + x))

    return minSum

print(solution([8, 5, 3, 4, 6, 8]))
print(solution([-100, 100])) 
print(solution([-100])) 
print(solution([10]))
print(solution([1,4,-3]))
print(solution([-8, 4, 5, -10, 3]))