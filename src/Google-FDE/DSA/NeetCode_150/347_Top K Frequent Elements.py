import heapq
from collections import Counter, defaultdict


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        newCounter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

        result = []

        for i in range(k):
            num,count = list(newCounter.items())[i]
            result.append(num)

        return result



    def _topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counter = Counter(nums)
        k_most_common = counter.most_common(k)
        return k_most_common



s = Solution()
print(s.topKFrequent([1,1,1,2,2,3,4,5], 2))
