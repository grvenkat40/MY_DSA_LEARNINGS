# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root):
        def helper(node):
            if node is None:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val == 0:
                if not node.left and not node.right:
                    return None
            return node
        return helper(root)

root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

obj = Solution()

res = obj.pruneTree(root)

def tree(node, l):
    if node.left:
        tree(node.left, l+1)
    print("     "*l, node.val)
    if node.right:
        tree(node.right, l+1)

tree(res, 0)