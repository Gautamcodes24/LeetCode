# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = [root.val]
        def getmax(root):
            if not root:
                return 0
            leftSum = getmax(root.left)
            rightSum = getmax(root.right)
            leftSum = max(leftSum , 0)
            rightSum = max(rightSum , 0)
            max_sum[0] = max(max_sum[0],root.val + leftSum + rightSum)
            return root.val + max(leftSum , rightSum)
        getmax(root)
        return max_sum[0]
