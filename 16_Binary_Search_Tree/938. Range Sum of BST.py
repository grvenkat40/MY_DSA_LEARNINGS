# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def helper(node):
            if node is None:
                return 0
            if node.val < low:
                return helper(node.right)
            elif node.val > high:
                return helper(node.left)
            else:
                return (node.val + helper(node.left) + helper(node.right))
        return helper(root)

node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(15)
node.left.left = TreeNode(3)
node.left.right = TreeNode(7)
node.right.right = TreeNode(18)

obj = Solution()
print(obj.rangeSumBST(node, 7, 15))