# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        res = []
        def helper(node, rem, path):
            if node is None:
                return None
            path.append(node.val)
            rem -= node.val
            if node.left is None and node.right is None:
                if rem == 0:
                    res.append(path.copy())
            helper(node.left, rem, path)
            helper(node.right, rem, path)
            path.pop()
        helper(root, targetSum, [])
        return res

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
print(obj.pathSum(root, 22))