
from collections import Counter

# 1. dict count
def most_frequent_with_dict(chars):
    counts = Counter(chars)
    return max(counts.values())

def most_frequent_brute_force(chars):

    mf = 0
    C = len(chars)

    for i in range(C):
        curr = 0
        for j in range(C):
            if chars[i] == chars[j]:
                curr += 1

        mf = max(mf, curr) 

    return mf



data = ['A', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C']

print(most_frequent_brute_force(data))
# print(most_frequent_with_dict(data))