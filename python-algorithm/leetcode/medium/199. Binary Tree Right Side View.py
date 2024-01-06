from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        depth_to_val = {}

        queue = deque()
        queue.append((0, root))

        while queue:
            depth, cur_node = queue.popleft()
            if cur_node is None:
                continue
            depth_to_val[depth] = cur_node.val

            if cur_node.left is not None:
                queue.append((depth + 1, cur_node.left))
            if cur_node.right is not None:
                queue.append((depth + 1, cur_node.right))

        return list(depth_to_val.values())


node4 = TreeNode(4)
node3 = TreeNode(3, None, node4)
node5 = TreeNode(5)
node2 = TreeNode(2, None, node5)
node1 = TreeNode(1, node2, node3)

solution = Solution()
view = solution.rightSideView(node1)
print(view)
