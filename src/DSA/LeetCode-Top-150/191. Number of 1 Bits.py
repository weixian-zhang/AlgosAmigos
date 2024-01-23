class Solution:
    def hammingWeight(self, n: int) -> int:

        return len([x for x in str('{0:b}'.format(n)) if x == '1'])
        