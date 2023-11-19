# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recursive(self, node):
        if node is None:
            return 0

        left_length = self.recursive(node.left)
        right_length = self.recursive(node.right)

        return max(left_length, right_length) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_length = self.recursive(root.left)
        right_length = self.recursive(root.right)
        root_result = left_length + right_length

        left_result_length = self.diameterOfBinaryTree(root.left)
        right_result_length = self.diameterOfBinaryTree(root.right)

        return max(root_result, left_result_length, right_result_length)


node4 = TreeNode(4)
node5 = TreeNode(4)
node2 = TreeNode(2, node4, node5)

node3 = TreeNode(3)

root = TreeNode(1, node2, node3)

solution = Solution()
print(solution.diameterOfBinaryTree(root))
