# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def helper(node):
            if not node: return 0   
            return 1+ max(helper(node.left),helper(node.right))
    
        l_h = helper(root.left)
        r_h = helper(root.right)

        return abs(l_h - r_h) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
