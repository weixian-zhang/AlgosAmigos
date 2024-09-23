from typing import List

# brute force backtracking to generate permutations - Memory Limit Exceeded
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        permutations = set()
        lenOfWords = len(''.join(words))
        result = []

        def wordLen(w: List[str]):
            return len(''.join(w))
        
        
        def backtracking_permutation(words: List[str], concatWords: List[str]):
            nonlocal permutations

            if wordLen(concatWords) == lenOfWords:
                permutations.add(''.join(concatWords))
                return
            
            for idx in range(len(words)):

                concatWords.append(words[idx])
                newWords = words.copy()
                newWords.pop(idx)
                backtracking_permutation(newWords, concatWords)

                concatWords.pop()


        
        # create permutation of words and store in set
        backtracking_permutation(words, [])
        

        # use sliding window where window size is concatenated words length to match against permutation set
        window_size = lenOfWords

        idx = 0
        while idx + window_size <= len(s):

            if s[idx:idx + window_size] in permutations:
                result.append(idx)
            
            idx += 1
                
        return result
    
    # Runtime: 4080 ms, faster than 41.90% of Python3 online submissions for Substring with Concatenation of All Words.
    # Memory Usage: 17.1 MB, less than 78.35% of Python3 online submissions for Substring with Concatenation of All Words.
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        result = []

        wordBank = {w:0 for w in list(set(words))}
        for w in words:
            if w in wordBank:
                wordBank[w] += 1

        eachWordLen = len(words[0])
        window_size = len(''.join(words))

        idx = 0
        while idx + window_size <= len(s):

            substring = s[idx:idx + window_size]
            
            subIdx = 0
            
            tempBank = wordBank.copy()
            while subIdx <= len(substring):
                eachWord = substring[subIdx:subIdx + eachWordLen]
                if eachWord in wordBank and tempBank[eachWord] > 0:
                    tempBank[eachWord] -= 1
     
                subIdx += eachWordLen

            if sum(list(tempBank.values())) == 0:
                result.append(idx)
            
            idx += 1

        return result




s = Solution()
print(s.findSubstring("ababaab", ["ab","ba","ba"])) #
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(s.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"]))
print(s.findSubstring('barfoothefoobarman', ["foo","bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))

# barfoo foobarthefoobarman
#        6  9
