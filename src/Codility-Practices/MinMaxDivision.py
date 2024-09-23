# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# binary search
def solution(K, M, A):
    
    minSumInBlock = max(A)
    maxSumInBlock = sum(A)

    while minSumInBlock <= maxSumInBlock:
        guessMaxSum = (maxSumInBlock + minSumInBlock) // 2

        if is_num_of_blocks_under_K_given_guessed_max_sum(K, guessMaxSum, A):
            maxSumInBlock = guessMaxSum - 1
        else:
            minSumInBlock = guessMaxSum + 1
    
    return minSumInBlock

def is_num_of_blocks_under_K_given_guessed_max_sum(blocksK, guessMaxSum, A):
    currSum = 0
    blocks = 0

    for x in range(len(A)):
        currSum += A[x]
        if currSum > guessMaxSum:
            blocks += 1
            currSum = A[x]

    return blocks < blocksK

# sliding window
# def solution(K, M, A):
#     # Implement your solution here

#     winSize = (len(A) // K)

#     maxSum = 0

#     for x in range(len(A) - winSize):
#         # check if next-next window is out of range, then increase windows size to get all
#         # "rest" of element
#         if (len(A) - 1) - x == winSize:
#             maxSum = max(sum(A[x+1:]), maxSum)
#             break

#         maxSum = max(sum(A[x: x + winSize]), maxSum)

#     return maxSum
    


solution(3, 5, [2,1,5,1,2,2,2])
#solution(5, 20, [6,8,4,10,20,1])