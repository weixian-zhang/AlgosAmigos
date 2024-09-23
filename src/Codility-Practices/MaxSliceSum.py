# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# use Kadane's algorithm
def solution(A):
    # Implement your solution here
    
    max_sum = A[0]
    curr_sum = max_sum

    for x in range(1, len(A), 1):

        # to retain previous Max or decide to start the current num as New Max
        curr_sum = max(curr_sum + A[x], A[x])
        max_sum = max(curr_sum, max_sum)

    return max_sum

# use Prefix Sum
def solution(A):

    prefixSum = [0 for x in range(len(A))]
    prefixSum[0] = A[0]
    max_sum = A[0]

    for x in range(1, len(A), 1):
       prefixSum[x] = A[x] + prefixSum[x - 1]
       max_sum = max(prefixSum[x], max_sum)

    return max_sum

solution([3,2,-6,4,0])
