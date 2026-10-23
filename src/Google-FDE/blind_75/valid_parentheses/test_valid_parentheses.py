import unittest
from valid_parentheses import Solution


# ''
# (
# ((
# ))
# ([])
# (({[]}))


class TestValidParenthesis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(''))

    def test_only_ob_ob(self):
        self.assertFalse(self.solution.isValid("(("))

    def test_only_close_parentheses_without_open(self):
        self.assertFalse(self.solution.isValid("))"))

    def test_ob_sb_csb_cob(self):
        self.assertTrue(self.solution.isValid("([])"))


    def test_ob_sb_cob(self):
        self.assertFalse(self.solution.isValid("([)"))

