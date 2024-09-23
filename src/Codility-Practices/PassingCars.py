
# 50% - O(N2)
# correctness = 100%
# performance = 0%
def solution(A):
    # Implement your solution here

    if len(A) == 1:
        return 0
    
    passingCars = 0
    lanes = {}
    for idx, x in enumerate(A):
        lanes[idx] = x

    carPairs = []

    for i in range(len(A)):
        for j in range(i + 1,len(A)):
            if A[i] == 1:
                break
            if A[i] < A[j]:
                carPairs.append((i, j))

    for _, cp in enumerate(carPairs):

        p = cp[0]
        q = cp[1]

        if (lanes[p] == 0 and lanes[q] == 1 or
            lanes[p] == 1 and lanes[q] == 0):
            passingCars += 1

        if passingCars > 1000000000:
            return -1
        
    return passingCars

# 100% - O(N)
def solution(A):

    sumEast = 0
    sumCrossing = 0

    for x in range(len(A)):
        # -> East
        if A[x] == 0:
            sumEast += 1
        # <= West
        if A[x] == 1:
            sumCrossing += sumEast

    if sumCrossing > 1000000000:
        return -1
    
    return sumCrossing

# print(solution([0, 0, 0, 0]))
# print(solution([0, 1, 0]))
# print(solution([0]))
print(solution([0,1,0,1,1]))
print(solution([0,1,1,1,1,0,1,1,1,1]))