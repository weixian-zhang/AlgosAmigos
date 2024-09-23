
# brute force method
# 100% correctness
# 25% perf
def solution(A):

    max_sum = 0

    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            max_sum = max(A[j] - A[i], max_sum)

    return max_sum


# # dynamic programming + memoization
# def dp_recursion(A: list[int], buyAtIdx: int, max_sum: list[int]):
    
#     if buyAtIdx < 0:
#         return max_sum
    
#     for x in range(len(A) - 1, 0, -1):
#         curr_sum = A[x] - A[buyAtIdx]
#         max_sum = max(max_sum, curr_sum)
#         dp_recursion(A,buyAtIdx - 1, max_sum )

#     return max_sum

# # dynamic programming + memoization
# def solution(A):
#     max_sum = dp_recursion(A, len(A) - 2, 0)
#     return max_sum

# 2 pointers
# if price at "sell day" < "buy day", use the "sell day" as the "new buy day"
# buy at the lowest price, if a sell day is lower than buy day, then no longer need to
# consider the buy day, move to new by day and consider again
# def solution(A):

#     max_sum = 0
#     buyDay, sellDay = 0, 1

#     while buyDay <= sellDay <= len(A) - 1:

#         if A[sellDay] < A[buyDay]:
#             buyDay = sellDay
#             sellDay += 1
#         else:
#             max_sum = max(max_sum, A[sellDay] - A[buyDay])
#             sellDay += 1

#     return max_sum





solution([23171, 21011, 21123, 21366, 21013, 21367])
