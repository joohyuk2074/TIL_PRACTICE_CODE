# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return

        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)

        return self.result


node3 = TreeNode(3)
node2 = TreeNode(2, node3, None)
node1 = TreeNode(1, None, node2)

solution = Solution()
solution.inorderTraversal(node1)
print(solution.result)
