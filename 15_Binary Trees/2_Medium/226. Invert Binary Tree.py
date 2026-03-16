from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        def helper(node):
            if node is None:
                return 
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)
        helper(root)
        return root

node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

obj = Solution()
print(obj.invertTree(node))