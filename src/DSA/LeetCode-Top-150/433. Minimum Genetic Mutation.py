from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque

        if startGene == endGene:
            return -1

        visited = set()
        bank = set(bank)
        
        # get list of mutated chars
        mutatedIndexes = []
        for x in range(len(startGene)):
            if startGene[x] != endGene[x]:
                mutatedIndexes.append(x)

        queue = deque([(startGene, 0)])

        

        while queue:

            currString, mutationCount = queue.popleft()

            if (currString == endGene):
                return mutationCount 

            for gs in ['A', 'C', 'G', 'T']:

                # all possible 32 mutations, 8 char-string * 4 possible gene-string
                for x in range(len(currString)):
                    newMutate = currString[:x] + gs + currString[x+1:]



                    if newMutate in bank and newMutate not in visited:
                        visited.add(newMutate)
                        queue.append((newMutate, mutationCount + 1))
                        

        return -1






s = Solution()





print(s.minMutation("AACCGGTT",
                    "AAACGGTA",
                    ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
# print(s.minMutation("AACCTTGG","AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"] ))
# print(s.minMutation("AACCGGTT", "AACCGCAA", ["AACCGGTA","AACCGGAA","AACCGCAA"]))
# print(s.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
# print(s.minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))