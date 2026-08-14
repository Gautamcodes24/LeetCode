# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return root
        q = deque([(root , root.val)])
        good_node = 0
        while q:
            popped_nd , max_val = q.popleft()
            if popped_nd.val >= max_val:
                good_node += 1
            curr_max = max(max_val,popped_nd.val)
            if popped_nd.left:
                q.append((popped_nd.left,curr_max))
            if popped_nd.right:
                q.append((popped_nd.right,curr_max))
        return good_node
            
        