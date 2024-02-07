# https://www.google.com/amp/s/www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/amp/

class Solution:
  def k_most_frequent(arr, k):
    from collections import defaultdict

    kTracker = defaultdict(int)

    for x in arr:
      kTracker[x] = kTracker[x] + 1

        
    kTupleList = sorted(kTracker.items(), key = lambda x: x[1], reverse=True)

    kSortedList = [x[0] for x in kTupleList]

    result = kSortedList[:k]

    return result

s = Solution
print(s.k_most_frequent( [3, 1, 4, 4, 5, 2, 6, 1], 2))

