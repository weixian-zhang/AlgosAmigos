# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# brute force O(n2)
def solution(A):

    if not A:
        return 0
    if len(A) == 1:
        return A[0]
    
    minDiff = 1000000

    idx = 0
    while idx <= len(A) - 2:

        minDiff = min(abs(sum(A[:idx + 1]) - sum(A[idx + 1:])), minDiff)
        idx += 1
                      
    return minDiff

# efficient method - get total first
# use total - "left partition" to get "right"
def solution(A):

    if not A or len(A) == 1:
        return 0

    sumAll = sum(A)
    minDiff = 1000000
    leftSum = 0

    for x in range(len(A) - 1):
       leftSum += A[x]
       rightSum = sumAll - leftSum
       diff = abs(leftSum - rightSum)
       minDiff = min(minDiff, diff)

    return minDiff

# def solution(A):
#     # Implement your solution here
    
#     A.sort()
#     sumNums = sum(A)

#     midPointToParition = sumNums // 2

#     leftSum = 0

#     idx = 0
#     while leftSum <= midPointToParition and (leftSum + A[idx]) <= midPointToParition:
#         leftSum += A[idx]
#         idx += 1
    
#     rightSum = sum(A[idx:])
    
#     return abs(rightSum - leftSum)

#print(solution([1, 2, 3, 4, 2]))
#print(solution([-1000,1000]))
print(solution([3,1,2,4,3]))
#print(solution([5,12,40,8,1,7]))