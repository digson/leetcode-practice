# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        sol = []
        
        def helper(node,sol):
            if node:
                helper(node.left, sol)
                sol.append(node.val)
                helper(node.right, sol)
        helper(root, sol)
        return sol
if __name__ == "__main__":
    s = Solution()
    # Test Case 1: Standard case
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert s.inorderTraversal(root1) == [1, 3, 2]
    
    # Test Case 2: Empty tree
    assert s.inorderTraversal(None) == []
    
    # Test Case 3: Single node tree
    root2 = TreeNode(5)
    assert s.inorderTraversal(root2) == [5]

    print("All test cases passed!")          