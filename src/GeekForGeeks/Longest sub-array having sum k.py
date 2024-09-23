
# https://www.geeksforgeeks.org/longest-sub-array-sum-k/
# Given an array arr[] of size n containing integers.
# The problem is to find the length of the longest sub-array having sum equal to the given value k.

# brute force - O(n2)
def lenOfLongSubarr(arr, K):
    
    N = len(arr)
    longest = 0 

    for i in range(N):
        tempSum = arr[i]
        for j in range(i + 1, N):
            tempSum +=  arr[j]
            if tempSum == K:
                longest = max(longest, (j - i) + 1)

    return longest

# Prefix Sum + reverse math Sum - K to get the "previous" stored in Dict
# O(N)
def lenOfLongSubarr(arr, K):
    
    N = len(arr)
    cumulativeSums = {}
    prefixSum = 0
    longest = 0

    for x in range(N):
        
        prefixSum += arr[x]

        if prefixSum == K:
            longest = max(x + 1, longest)
        
        elif (prefixSum - K) in cumulativeSums:
            prevIdxOfSum = cumulativeSums[prefixSum - K]
            longest = max(longest, x - prevIdxOfSum)

        if prefixSum not in cumulativeSums:
            cumulativeSums[prefixSum] = x

    return longest





print(lenOfLongSubarr([1,2,3,1,1,1,1,4,2,3], 3))
print(lenOfLongSubarr([10, 5, 2, 7, 1, 9], 15))
print(lenOfLongSubarr([-5, 8, -14, 2, 4, 12], -5))