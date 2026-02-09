# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.result = 0
        def maxDepth(node):
            if node is None:
                return 0
            LHS = maxDepth(node.left)
            RHS = maxDepth(node.right)
            self.result = max(self.result, (LHS+RHS))
            return 1+max(LHS, RHS)
        maxDepth(root)
        return self.result

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)
node.left.right.left = TreeNode(8)
node.right.left.left = TreeNode(9)
node.right.right.right = TreeNode(10)

obj = Solution()
print(obj.diameterOfBinaryTree(node))