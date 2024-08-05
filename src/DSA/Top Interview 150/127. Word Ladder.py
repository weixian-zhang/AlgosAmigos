from typing import List
from collections import defaultdict, deque

class Solution:

    # almost successful, but ajacency list neighbours are in correct
    # as the 1 char difference has to be in order
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    #     if endWord not in wordList or not endWord or not beginWord or not wordList:
    #         return 0
        
    #     def one_word_diff(a: str, b: str) -> bool:
    #         b = list(b)
    #         for w in a:
    #             if w in b:
    #                 b.pop(b.index(w))

    #         return True if len(b) == 1 else False


    #     # create adjacency list of word relations
    #     #unqWL = wordList #list([beginWord] + wordList)
    #     adjacencyList = { x:[] for x in wordList }

    #     for word, _ in adjacencyList.items():
    #         for w in wordList:
    #             if word == w:
    #                 continue
    #             if one_word_diff(word, w):
    #                 adjacencyList[word].append(w)

    #     # BFS
    #     queue = Deque([])
    #     visited = set([beginWord])
    #     path = []
    #     queue.append((beginWord, [beginWord]))

    #     while queue:

    #         currWord, path = queue.popleft()

    #         if currWord == endWord:
    #             return len(path)

    #         for neighbour in adjacencyList[currWord]:
    #             if neighbour not in visited:
    #                 visited.add(currWord)
    #                 queue.append((neighbour, path + [neighbour]))
                    
        
    #     return 0
    
    # concept from neetcode 
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        

        adjList = defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '_' + w[i+1:]
                adjList[pattern].append(w)

        visited = set([beginWord])
        path = [beginWord]
        queue = deque([(beginWord,path)])
                      
        while queue:
            
            # pop queue "horizontally"
            for i in range(len(queue)):

                currWord, path = queue.popleft()

                if currWord == endWord:
                    return len(path)
                
                for j in range(len(currWord)):
                    currWordPattern = currWord[:j] + '_' + currWord[j+1:]

                    for neighbour in adjList[currWordPattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append((neighbour, path + [neighbour]))

        return 0

s = Solution()

# print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot", "log","cog"])) #",

#print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))

print(s.ladderLength('leet', 'code', ["lest","leet","lose","code","lode","robe","lost"]))

