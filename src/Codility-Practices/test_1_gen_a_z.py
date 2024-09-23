# Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.
# Examples:
# 1. Given N = 3, the function may return "fig", "pea", "nut", etc. Each of these
# strings contains three different letters with the same number of occurrences
# 2 Given N = 5, the function may return "mango", "grape", "melon", etc. 3. 
# Given N = 30, the function may return "aabbcc. oo" (each letter from 'a' to 'o' occurs twice).
    #The string contains 15 different letters
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1. 200,000]

def solution(N):
    import string

    a_z = string.ascii_lowercase

    numOfLettersToRepeat = ''
    if N <= 26:
        numOfLettersToRepeat = ''.join(a_z[:N])
        return numOfLettersToRepeat
    
    numOfLettersToRepeat = N
    timeToRepeat = 1
    while numOfLettersToRepeat > 26:
        timeToRepeat *= 2
        numOfLettersToRepeat = numOfLettersToRepeat // 2

    lettersRepeating = ''.join(a_z[:numOfLettersToRepeat])

    lettersRepeating *= (timeToRepeat + 1)
    

    # while len(lettersRepeating) + numOfLettersToRepeat <= N:
    #     lettersRepeating += a_z[:numOfLettersToRepeat]

    remainders = N - len(lettersRepeating)
    lettersRemaining = a_z[:remainders]

    sortedResult = ''.join(sorted(lettersRepeating + lettersRemaining))

    return sortedResult

# def solution(N):
#     import string

#     a_z = string.ascii_lowercase

#     numOfLettersToRepeat = ''

#     if N <= 26:
#         lettersToRepeat = ''.join(a_z[:N])
#     else:
#         remainder = ''.join(a_z[: N % 26])
#         lettersToRepeat = ''.join(a_z * (N // 26))
#         lettersToRepeat += remainder

#     sortedResult = ''.join(sorted(lettersToRepeat))

#     return sortedResult
        
# def solution(N):
#     import string

#     a_z = string.ascii_lowercase

#     #divisor = get_largest_divisor(N)

#     #charsToRepeat = divisor % 26

#     if N < 26:
#         return str(a_z[:N])
    
#     charsToRepeat = N % 26

#     letters = a_z[:charsToRepeat] * divisor

#     sortedResult = ''.join(sorted(letters))

#     return sortedResult


# print(len(solution(30)))
# print(len(solution(1)))
# print(len(solution(3)))
# print(len(solution(5)))
# print(len(solution(30)))
# print(len(solution(60)))
print(len(solution(1000)))
print(len(solution(703)))
