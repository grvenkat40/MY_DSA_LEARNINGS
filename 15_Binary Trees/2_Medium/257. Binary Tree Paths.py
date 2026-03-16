# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        if root is None:
            return []
        res = []
        def helper(node, path):
            if node is None:
                return 
            path += str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
            path += "->"
            helper(node.left, path)   
            helper(node.right, path)
        helper(root, "")
        return res

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.right = TreeNode(5)

obj = Solution()
print(obj.binaryTreePaths(node))