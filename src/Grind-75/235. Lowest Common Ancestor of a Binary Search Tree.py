# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def _dfs(node, target, path):

            if not node:
                return False

            path.append(node)

            if node.val == target.val:
                return True

            is_node_in_left = _dfs(node.left, target, path)

            is_node_in_right = _dfs(node.right, target, path)

            if is_node_in_left or is_node_in_right:
                return True

            path.pop(-1)

            return False


        p_path = []

        q_path = []

        _dfs(root, p, p_path)

        _dfs(root, q, q_path)


        i, j = 0, 0

        while i <= len(p_path) -1 and j <= len(q_path) - 1:
            if p_path[i].val == q_path[j].val:
                i += 1
                j += 1
            else:
                break

        return p_path[i-1]

        
            
        