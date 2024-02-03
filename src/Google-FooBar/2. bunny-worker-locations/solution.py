# Keeping track of Commander Lambda's many bunny workers is starting to get tricky.
# You've been tasked with writing a program to match bunny worker IDs to cell locations.

# The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station,
# and as a result the work areas have an unusual layout.
# They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

# For example, 
    # the bunny worker at (1, 1) has ID 1, 
    # the bunny worker at (3, 2) has ID 9, 
    # and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers).

# Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y).
# Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.


# -- Python cases --
# Input:
# solution.solution(5, 10)
# Output:
#     96

# Input:
# solution.solution(3, 2)
# Output:
#     9

# https://medium.com/@fahnub/taking-on-googles-foobar-challenge-dab4f7a4da78
# https://codereview.stackexchange.com/questions/200535/finding-the-position-in-a-triangle-for-the-given-challenge
# https://anush-venkatakrishna.medium.com/bunny-prisoner-locating-9b5b22c5fce7

# https://www.khanacademy.org/math/in-in-grade-10-ncert/x573d8ce20721c073:arithmetic-progressions/x573d8ce20721c073:intro-to-arithmetic-progressions/e/arithmetic_sequences_1
# https://www.youtube.com/watch?v=WH9BDmHmqXA

# O(n2) solution - create a matrix
# def solution(x, y):

#     id =  (((x + y - 2) * (x + y - 1)) / 2) + x

#     # 100,000 is 40,000 cols
#     matrixInit = False
#     bunnies = 100000
#     rows = 450
#     matrix = [[0 for _ in range(rows)] for _ in range(rows)]
#     C = len(matrix[0])
#     R = len(matrix)

#     # create lower triangle matrix
#     def create_bunny_workplace(matrix):
#         # arrange numbers as lower triangle ascending diagonally up
#         num = 1
#         for i in range(len(matrix) - 1, -1, -1):

#             # for every i, j = i + 1 but inversed
#             col = (len(matrix) - 1 - i) + 1

#             for j in range(col):
                
#                 # shift number down if the cell below is 0
#                 while (i + 1) <= R - 1 and matrix[i + 1][j] == 0:
#                     i += 1

#                 matrix[i][j] = num
#                 num  += 1

#                 if matrix[i][j] == bunnies:
#                     matrixInit = True
#                     return matrix
                
#     if not matrixInit:
#         matrix = create_bunny_workplace(matrix)
    
#     newY = R - y
#     newX = x - 1

#     id = matrix[newY][newX]

#     return str(id)

def solution(x, y):

    # find starting point by getting nth/xth term of AP
    # the formula (n)*(n-1) / 2 works by finding Xth term value of x-1. So e.g: to find xth term of 3, n will be 4
    # (4*(4-1)) / 2 = 6

    x += 1
    xthTermValue = (x * (x - 1)) // 2

    x -= 1
    startOfCommonDiff = x

    bunnyId = xthTermValue

    # common differenceis 1, so add 1 to the start of common difference up till (Y - 1)
    # python will exclude 1 from Y already, so no need to Y-1
    for x in range(startOfCommonDiff, (y + startOfCommonDiff) - 1):
        bunnyId += x

    return str(bunnyId)

print(solution(4,1)) 
print(solution(4,7)) 
print(solution(1,1))
print(solution(3,7))
print(solution(1,6))  # 1
print(solution(3,2))  # 9
print(solution(2,3))  # 8
print(solution(1,4))  # 7
print(solution(7,16))   # 238
print(solution(10,24))   # 538