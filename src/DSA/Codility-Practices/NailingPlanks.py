# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A, B, C):
#     # Implement your solution here
#     result = 0
#     planks = {}
#     B = B[:len(A)] # contraint: A <= B

#     # list of tuple of planks
#     for x in range(len(A)):
#         start, end = A[x], B[x]
#         for p in range(start, end + 1):
#             planks[p] = p

#     for _, c in enumerate(C):

#         target = c

#         if not planks:
#             return result

#         # binary search
#         low, high = list(planks.keys())[0], list(planks.keys())[-1]

#         while low <= high:
#             mid = (high + low) // 2

#             if planks[mid] == target:
#                 result += 1
#                 for x in range(1, target + 1):
#                     if x in planks:
#                         del planks[x]
#                 break
#             elif planks[mid] > target:
#                 high = mid - 1
#             else:
#                 low = mid + 1

#     return result

def solution(A, B, C):

    result = -1

    A.sort()
    B.sort()
    C = list(set(C))

    for _, n in enumerate(C):

        i = 0
        while A and i <= len(A) - 1:
            if n in range(A[i], B[i] + 1):
                A.pop(i)
                B.pop(i)
                i = 0
                if result == -1:
                    result = 1
                else:
                    result += 1
            else:
                i += 1

    return -1 if A else result





    

     

print(solution([2],[2], [1]))
print(solution([1,4,5,8],[4,5,9,10], [4,6,7,10,2]))
