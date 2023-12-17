# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):

    if len(H) == 1:
        return 1

    # Implement your solution here
    minHeight = max(H[0], H[-1])
    blocks = 1
    lowBlocks = []

    for x in range(1, len(H)):

        height = H[x]

        if lowBlocks:
            if sum(lowBlocks) + height >= minHeight:
                blocks += 1
                lowBlocks = []
            else:
                lowBlocks.append(height)
        else:
            if height >= minHeight:
                blocks += 1
            else:
                lowBlocks.append(height)

    return blocks



H = [6,47,8,8,8,8,6]  
# H = [6,6]
# H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
#H = [8,8,5,3,9,8,7,4,8]
print(solution(H))