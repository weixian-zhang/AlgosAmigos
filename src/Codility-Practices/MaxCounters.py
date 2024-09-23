# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
# correctness - 100% 
# performance - 100%, O(N)
def solution(N, A):
    # Implement your solution here
    
    curr_max = 0
    lastUpdatedMax = 0
    counters = {}
    for x in range(1, N + 1):
        counters[x] = 0

    for x in range(len(A)):
         
         counter = A[x]

         if counter <= N:
             counters[counter] = max(lastUpdatedMax, counters[counter]) + 1
             curr_max = max(curr_max, counters[counter])
             
         else:
             lastUpdatedMax = curr_max

    for k, _ in counters.items():
        counters[k] = max(lastUpdatedMax, counters[k])
                 

    return list(counters.values())

# print(solution(20, [5,6, 20]))
# print(solution(2, [5,6]))
# print(solution(1, [6,6]))
print(solution(5, [3,4,4,6,1,4,4, 6, 3, 1, 2]))