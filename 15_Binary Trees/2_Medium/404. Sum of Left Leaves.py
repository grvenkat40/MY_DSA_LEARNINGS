# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.total = 0
        def helper(node, flag):
            if node is None:
                return None
            helper(node.left, 0)
            if node.left is None and node.right is None:
                if flag == 0:
                    self.total += node.val
            helper(node.right, 1)
        helper(root, -1)
        return self.total

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

obj = Solution()
print(obj.sumOfLeftLeaves(node))