from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ascii_group = []

        for w in strs:
            sorted_w = ''.join(sorted(w))
            ascii_group.append(((sorted_w, w)))

        groups = defaultdict(list)
        for asciiSum, word in ascii_group:
            groups[asciiSum].append(word)

        
        result = [words for words in groups.values()]

        return result





# s = Solution()
# print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # ''
    def test_empty(self):
        self.s.groupAnagrams('')

    # 'a'
    def test_a(self):
        self.s.groupAnagrams('a')
    

    # 'aa'
    def test_aa(self):
        self.s.groupAnagrams(['aa'])
    

    # "eat","tea","tan","ate","nat","bat"
    def test_1(self):
        self.s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
