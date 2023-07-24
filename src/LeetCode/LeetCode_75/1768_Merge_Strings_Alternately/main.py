class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []

        word1Len = len(word1) - 1
        word2Len = len(word2) - 1
        word2Idx = 0
        for idx, s in enumerate(word1):
            
            result.append(s)
            
            if idx <= word2Len:
                result.append(word2[idx])
                word2Idx = idx
                continue

        if word1Len  < word2Len:
            result.append(word2[word2Idx+1:])

        return ''.join(result)
    
if __name__ == '__main__':
    s = Solution()
    r = s.mergeAlternately('abcd', 'pq')
    print(r)
