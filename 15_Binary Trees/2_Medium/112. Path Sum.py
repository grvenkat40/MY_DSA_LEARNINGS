# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def helper(node, total):
            if node is None:
                return False
            total += node.val
            if not node.left and not node.right:
                return total == targetSum
            return helper(node.left, total) or helper(node.right, total)
        return helper(root, 0)

root = TreeNode(5)

root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

obj = Solution()
print(obj.hasPathSum(root, 22))