# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root, low: int, high: int):
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low , high)
        if root.val > high:
            return self.trimBST(root.left, low , high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

node = TreeNode(4)
node.left = TreeNode(1)
node.left.left = TreeNode(0)
node.left.right = TreeNode(2)
node.left.right.right = TreeNode(3)
node.right = TreeNode(6)
node.right.left = TreeNode(5)
node.right.right = TreeNode(7)
node.right.right.left = TreeNode(8)

obj = Solution()

root = obj.trimBST(node, 1, 5)

def show(root, l):
    if root is None:
        return None
    show(root.left, l+1)
    print("     "*l, root.val)
    show(root.right, l+1)

show(root, 0)