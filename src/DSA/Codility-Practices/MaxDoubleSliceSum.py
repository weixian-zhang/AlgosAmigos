def solution(A):
#     # Implement your solution here
    
    klr = [0 for _ in range(len(A))]
    krl = [0 for _ in range(len(A))]

    curr_sum = 0
    
    # start at "2nd" element
    for x in range(1, len(A) - 1):
        curr_sum = max(A[x], A[x] + curr_sum)
        curr_sum = max(curr_sum, 0)
        klr[x] = curr_sum

    curr_sum = 0
    
    # start at "2nd" last element
    for x in range(len(A) - 2, 0, -1):
        curr_sum = max(A[x], A[x] + curr_sum)
        curr_sum = max(curr_sum, 0)
        krl[x] = curr_sum
        
    maxSumOf2Slices = 0

    for x in range(1, len(A) - 1): #range(1, len(A)-1):
       maxSumOf2Slices = max(klr[x - 1] + krl[x + 1], maxSumOf2Slices)
    
    return maxSumOf2Slices

# brute force
# correctness 88%
# X <-> Y <-> Z
# Y pointer will move from X+1 to Z-1, as Y moves, it partitions the slice into 2 partition X-Y and Y-Z
# summing left partition and 1 num each on right partition
def solution(A):

    if len(A) <= 3:
        return 0
    
    max_sum = 0
    x = 0
    y = 1
    z = len(A) - 2

    while x <= y <= z:

        xySum = sum(A[1:y])

        for yz in range(len(A) - 2, y, -1):
            zySlice = sum(A[y + 1:yz + 1])
            max_sum = max(xySum + zySlice, max_sum)
 
        max_sum = max(max_sum, xySum)
        y += 1

    return max_sum

# def solution(A):
#     N = len(A)
    
#     # Calculate the maximum sum ending at each position
#     max_ending_here = [0] * N
#     for i in range(1, N-1):
#         max_ending_here[i] = max(0, max_ending_here[i-1] + A[i])

#     # Calculate the maximum sum starting at each position
#     max_starting_here = [0] * N
#     for i in range(N-2, 0, -1):
#         max_starting_here[i] = max(0, max_starting_here[i+1] + A[i])

#     # Find the maximum double slice sum
#     max_double_slice_sum = 0
#     for i in range(1, N-1):
#         max_double_slice_sum = max(max_double_slice_sum, max_ending_here[i-1] + max_starting_here[i+1])

#     return max_double_slice_sum

# brute force
# def solution(A):
#     pass

print(solution([-2, -3, -4, 1, -5, -6, -7]))
# print(solution([6, 1, 5, 6, 4, 2, 9, 4]))
# print(solution([0,10,-5,-5,0]))
# print(solution([5, 0, 1, 0, 5]))
# print(solution([5, 5, 5]))
# print(solution([3,2,6,-1,4,5,-1,2]))