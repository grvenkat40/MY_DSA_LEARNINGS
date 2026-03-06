# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root) -> int:
        self.mini = float("inf")
        self.prev = None
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                self.mini = min(self.mini, node.val - self.prev.val)
            self.prev = node
            inorder(node.right)
        inorder(root)
        return self.mini

node = TreeNode(4)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right = TreeNode(6)

obj = Solution()
print(obj.minDiffInBST(node))