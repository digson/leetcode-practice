# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        sol = []

        def helper(root,sol):
            if not root: return
            sol.append(root.val)
            helper(root.left,sol)
            helper(root.right,sol)

        helper(root,sol)
        return sol
