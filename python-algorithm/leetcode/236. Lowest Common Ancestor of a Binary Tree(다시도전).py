# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        """
        if root == None:
            return None

        left_result = self.lowestCommonAncestor(self, root.left, p, q)
        right_result = self.lowestCommonAncestor(self, root.right, p, q)

        if left_result == p or right_result == q:
            return root
        elif left_result and right_result:
            return root
        elif left_result:
            return left_result
        elif right_result:
            return right_result
