# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# The solution obtained perfect score
def solution(A, K):
    # Implement your solution here
    
    Alen = len(A)
    # a list with same len as A. Values are updated to the new rotated index
    swapResult = [0 for x in range(Alen)]

    for idx, a in enumerate(A):

        newSwapIdx = (idx + K) % Alen
        swapResult[newSwapIdx] = a

    return swapResult


print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 3))
print(solution([1, 2, 3, 4], 4))

