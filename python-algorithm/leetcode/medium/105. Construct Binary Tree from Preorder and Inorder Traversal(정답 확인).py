# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder, inorder):

        def recursive(preStart, inStart, inEnd):
            if preStart > len(preorder) - 1 or inStart > inEnd:
                return None

            root = TreeNode(preorder[preStart])
            inIndex = 0
            for i in range(inStart, inEnd + 1):
                if inorder[i] == root.val:
                    inIndex = i

            root.left = recursive(preStart + 1, inStart, inIndex - 1)
            root.right = recursive(preStart + (inIndex - inStart + 1), inIndex + 1, inEnd)
            return root

        return recursive(0, 0, len(inorder) - 1)


# node15 = TreeNode(15)
# node7 = TreeNode(15)
# node20 = TreeNode(20, node15, node7)
# node9 = TreeNode(9)
# node3 = TreeNode(3, node9, node20)

solution = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree = solution.buildTree(preorder, inorder)
print(tree)
