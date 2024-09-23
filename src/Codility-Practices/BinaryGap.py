# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# The solution obtained perfect score
def solution(N):
    # Implement your solution here

    if N == 0:
        return 0
    
    # solution using 2 pointers start from far left
    maxZeros = 0
    anchor = 0
    forwarder = 1

    binary = bin(N)[2:]

    while forwarder <= len(binary) - 1:
        if binary[forwarder] == '0':
            forwarder += 1
            continue

        maxZeros = max(forwarder - (anchor + 1) , maxZeros)
        anchor = forwarder
        forwarder += 1

    return maxZeros

solution(0)
solution(9)
solution(529)
solution(20)
solution(32)
solution(15)
