class TrieNode:
    def __init__(self, char='') -> None:
        self.char = char
        self.children = {}
        self.isEndOfWord = False

# Runtime: 145 ms, faster than 56.50% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 31.4 MB, less than 74.92% of Python3 online submissions for Implement Trie (Prefix Tree).
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root

        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
                curr = curr.children[s]
                continue

            curr = curr.children[s]

        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        
        curr = self.root

        for s in word:
            if s not in curr.children:
                return False
            
            curr = curr.children[s]

        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root

        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]

        return True




# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
obj.insert('apples')
print(obj.search('apple'))
print(obj.startsWith('app'))