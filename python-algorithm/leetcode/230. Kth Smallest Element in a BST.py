# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.result = []

    def recursive(self, node):
        if node is None:
            return

        self.recursive(node.left)
        self.result.append(node.val)
        self.recursive(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.recursive(root)

        return self.result[k - 1]
