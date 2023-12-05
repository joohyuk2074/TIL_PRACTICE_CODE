# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.answer = {}

    def recursive(self, node, depth):
        if node is None:
            return

        if depth not in self.answer:
            self.answer[depth] = []
        self.answer[depth].append(node.val)

        self.recursive(node.left, depth + 1)
        self.recursive(node.right, depth + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.recursive(root, 0)

        result = []
        for key in self.answer:
            result.append(self.answer[key])
        return result
