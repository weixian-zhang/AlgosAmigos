
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end_of_word = True


    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

    def delete(self, word: str):

        def recursion(curr: TrieNode, i: int) -> bool:
            
            if i == len(word):
                if not curr.end_of_word:
                    return False
                curr.end_of_word = False
                return len(curr.children) == 0

            char = word[i]
            child = curr.children.get(char)

            if child is None:
                 return False
            
            can_remove_children = recursion(child, i + 1)

            if can_remove_children:
                del curr.children[char]

            return not curr.end_of_word and len(curr.children) == 0
        
    
        recursion(self.root, 0)

        
        
        


# Your Trie object will be instantiated and called as such:
word = 'apple'

obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith('app')
obj.delete('apple')