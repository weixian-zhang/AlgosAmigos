# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Runtime: 63 ms, faster than 38.60% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Memory Usage: 18.7 MB, less than 19.99% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # pre-order traversal
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        def _preorder(nums: list[int]):

            if not nums:
                return
            
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            mid = len(nums) // 2

            node = TreeNode(nums[mid])
            node.left = _preorder(nums[:mid])
            node.right = _preorder(nums[mid+1:])

            return node
        

        root =_preorder(nums)

        return root

    

s = Solution()
s.sortedArrayToBST([-10,-3,0,5,9])