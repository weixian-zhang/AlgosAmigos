# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    if not A:
        return 1

    # Implement your solution here
    A.sort()
    Aset = set(A)

    missing = 1

    while missing <= A[-1]:
        if missing not in Aset:
            return missing
        missing += 1
    
    return missing

print(solution([]))
print(solution([0]))
print(solution([1]))
print(solution([2]))
print(solution([2,3,1,5]))
print(solution([100, 50, 44, 30]))