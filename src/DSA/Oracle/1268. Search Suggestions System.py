from typing_extensions import List

class TrieNode:
    def __init__(self, char: str) -> None:
        self.char = char
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode('')

    def add_word(self, word: str):
        
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c]= TrieNode(c)
            curr = curr.children[c]
        
        curr.isWord = True

    def starts_with(self, word: str) -> list[bool, TrieNode]:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False, None
            curr = curr.children[c]
        
        return True, curr
    

    def get_words_by_node(self, node: TrieNode, chars: str) -> list[str]:
        
        result = set()

        def dfs(tn: TrieNode):
            nonlocal chars

            if tn.isWord and len(result) < 3:
                result.add(chars)

            for k, n in tn.children.items():
                chars += k
                dfs(n)
                chars = chars[:-1]  # backtracking

        dfs(node)

        return list(result)


class Solution:

    # prefix tree
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for p in products:
            trie.add_word(p)
        
        result = []

        for x in range(1, len(searchWord)+1):
            w = searchWord[:x]

            isStartsWith, node = trie.starts_with(w)

            if not isStartsWith:
                result.append([])
                continue

            products = trie.get_words_by_node(node, w)
            products.sort()

            result.append(products)
        
        return result
    

s = Solution()

print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'))

        



