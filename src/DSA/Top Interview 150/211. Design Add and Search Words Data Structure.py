
class TrieNode:
    def __init__(self, char='') -> None:
        self.char = char
        self.children: dict = {}
        self.isEndOfWord = False

# my own solution
# Runtime: 2093 ms, faster than 52.07% of Python3 online submissions for Design Add and Search Words Data Structure.
# Memory Usage: 66.6 MB, less than 45.63% of Python3 online submissions for Design Add and Search Words Data Structure.
class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add(self, word: str):

        curr = self.root

        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
                curr = curr.children[s]
                continue

            curr = curr.children[s]

        curr.isEndOfWord = True

    def search_full_word(self, word):
        
        curr = self.root

        for s in word:
            if s not in curr.children:
                return False
            
            curr = curr.children[s]

        return curr.isEndOfWord


    def search(self, prefix: str, node: TrieNode):

        curr = node
    
        for wIdx, s in enumerate(list(prefix)):
            
            # wildcard
            if s == '.':
                
                # get all chars
                for ws in curr.children.keys():
                    newPrefix = ws + prefix[wIdx + 1:]
                    # curr = curr.children[ws]
                    found = self.search(newPrefix, curr)
                    if found:
                        return True

            if s not in curr.children:
                return False
            
            if s != '.':
                curr = curr.children[s]
            else:
                return False
        
        return curr.isEndOfWord


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word, self.trie.root)
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
# obj.addWord('a')
# obj.addWord('a')
# print(obj.search('.a'))
# print(obj.search('a.'))

# obj.addWord('bad')
# obj.addWord('dad')
# obj.addWord('mad')
# print(obj.search('pad'))
# print(obj.search('bad'))
# print(obj.search('.ad'))
# print(obj.search('b..'))

# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
obj.addWord('bat')
print(obj.search('a'))
# print(obj.search('b.'))
# print(obj.search('a.d'))
# print(obj.search('.'))