from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        current_level = 1
        max_level = 1
        maximum = float('-inf')
        while q:
            q_len = len(q)
            level_sum = 0
            for _ in range(q_len):
                curr_node = q.popleft()
                level_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            if level_sum > maximum:
                maximum = level_sum
                max_level = current_level
            current_level += 1
        return max_level
        



        