
# using brute force method to find combination numbers which divides by len(A) + F = M
# time complexity - O(N2)
def int_to_array(num: int):
    return [int(x) for x in str(num)]

def solution(A, F, M):
    
    existingDiceSum = sum(A)

    divisor = len(A) + F

    arrF = []  # an element for each missing dice
    for _ in range(F):
        arrF.append([1, 7])

    # using recursion to generate cartesian product
    # or use  from itertools import product
    # for p in list(product([1,2,3,4,5,6], [1,2,3,4,5,6])):
    def cartesian_product(ranges, result, *args):

        # absecase
        if not ranges:
            result.append(args)
            return

        start, stop = ranges[0]
        for x in range(start, stop):
            cartesian_product(ranges[1:], result, *args + (x, ))

    cartesianProducts = []
    cartesian_product(arrF, cartesianProducts)

    for prod in cartesianProducts:
        prodList = list(prod)
        if (existingDiceSum + sum(prodList)) // divisor == M:
            return prodList
        
    return [0]

# def solution(A, F, M):
#     # Implement your solution here
#     divisor = len(A) + F  # divisor to get M

#     sumOfExistingResult = sum(A)

#     # start = int(''.join([str(1) for x in range(F)]))
#     # stop = int(''.join([str(6) for x in range(F)]))

#     # while start <= stop:
#     #     start += 1

#     #     arrNums = int_to_array(start)
#     #     if (sumOfExistingResult + sum(arrNums)) // divisor == M:
#     #         return arrNums

#     arrF = [1 for x  in range(F)]

#     idx = len(arrF) - 1
#     while idx >= 0:
        
#         for i in range(idx, idx + 1):
#         for roll in range(1,7):
#             pass
                
#         idx -= 1

#     return [0]


print(solution([3,2,4,3], 2, 4))
print(solution([1,5,6], 4, 3))  # 2,1,2,4
print(solution([1,2,3,4], 4, 6)) # not possible, return [0]


# references - recursion to generate number combination or cartesian products
#https://stackoverflow.com/questions/38068669/dynamic-for-loops-in-python

def dynamic_for_loop(boundaries, *vargs):
    if not boundaries:
        print(*vargs) # or whatever you want to do with the values
    else:
        bounds = boundaries[0]
        for i in range(*bounds):
          dynamic_for_loop(boundaries[1:], *(vargs + (i,)))

from itertools import product
for p in list(product([1,2,3,4,5,6], [1,2,3,4,5,6])):
    print(*p)


boundaries = [[1, 7, 1], [1, 7, 1], [1, 7, 1]] #,[1, 7, 1],[1, 7, 1],[1, 7, 1]]
dynamic_for_loop(boundaries)