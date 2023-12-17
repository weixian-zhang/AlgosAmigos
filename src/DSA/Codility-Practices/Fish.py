# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: list[int], B: list[int]):
    # Implement your solution here

    if not A:
        return 0

    # 0 -> upstream
    # 1 <- downstream
    meet = -1
    left, right = 0, 1

    # -1 represents dead, e.g A[idx] = -1

    while right > 0 and right <= len(A) - 1:

        # meet
        if B[left] != B[right]:
            # left bigger than right
            if A[left] > A[right]:
                meet = B[left]
                A[right] = -1
                right += 1
            else:
                meet = B[right]
                A[left] = -1
                right = left
                left -= 1
        else:
            # met and going upstream
            if meet == 0:
                if A[left] > A[right]:
                    A[right] = -1
                    
                #left += 1
                right += 1

            elif meet == 1:
                if A[left] < A[right]:
                    A[left] -= 1
                
                left -= 1
                #right -=1

            else:
                left += 1
                right += 1

    result = sum([1 for x in range(len(A)) if A[x] != -1])
    return result

A = [4,3,2,1,5]
B = [0,1,0,0,0]
print(solution(A, B))

