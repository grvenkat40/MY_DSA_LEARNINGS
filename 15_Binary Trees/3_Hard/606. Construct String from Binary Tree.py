# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root) -> str:
        self.res = ""
        def helper(node):
            if node is None:
                return
            self.res += str(node.val)
            if node.left is None and node.right is None:
                return
            self.res += '('
            helper(node.left)
            self.res += ')'
            if node.right:
                self.res += '('
                helper(node.right)
                self.res += ')'
        helper(root)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

obj = Solution()
print(obj.tree2str(root))