# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        def getDepth(root):
            if not root:
                return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            nonlocal max_dia
            max_dia = max(max_dia , left + right)
            return max(left,right) + 1
        getDepth(root)
        return max_dia