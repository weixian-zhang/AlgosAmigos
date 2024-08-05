from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self, char = '') -> None:
        self.char = ''
        self.children = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.isEndOfWord

    def starts_with(self, word: str):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

class Solution:

    # backtracking with Trie
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        R, C = len(board), len(board[0])
        visited = set()
        result = set()
        trie = Trie()
        for w in words:
            trie.insert(w)

        # going into this function, means into 1 cell, and foreach cell,
        # explore up,down,left,right cells
        def dfs(chars: str, i: int, j: int, node: TrieNode):

            # base case
            if ((i, j) in visited or
                i < 0 or j < 0 or
                i > (R-1) or j > (C-1) or
                board[i][j] not in node.children
                ):
                return
            
            visited.add((i, j))

            chars += board[i][j]
            
            node = node.children[board[i][j]]

            # if trie.search(chars):
            if node.isEndOfWord:
                result.add(chars)

            dfs(chars, i - 1, j, node)
            dfs(chars, i + 1, j, node)
            dfs(chars, i, j - 1, node)
            dfs(chars, i, j + 1, node)

            # backtrackmove previous and try new cell
            visited.remove((i,j))


        for i in range(R):
            for j in range(C):
                char = board[i][j]
                if not trie.starts_with(char):
                    continue
                
                dfs('', i, j, trie.root)
                
                
        return result


        

        




s = Solution()

# expected: []
#print(s.findWords([["a","a"]], ["aaa"]))

# expected: ["oa","oaa"]
print(s.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"]))

print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))