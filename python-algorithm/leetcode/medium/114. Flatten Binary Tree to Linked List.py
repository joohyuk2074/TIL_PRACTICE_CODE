# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.list = []

    def recursive(self, node):
        if node is None:
            return

        self.list.append(node)

        self.recursive(node.left)
        self.recursive(node.right)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.recursive(root)

        answer = None
        current_node = None
        for node in self.list:
            if current_node is None:
                answer = node
                current_node = node
                node.left = None
                node.right = None
            else:
                node.left = None
                node.right = None
                current_node.right = node
                current_node = node

        return answer

