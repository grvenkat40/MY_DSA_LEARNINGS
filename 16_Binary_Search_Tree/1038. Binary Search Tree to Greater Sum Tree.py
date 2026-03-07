# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root):
        if root is None:
            return None
        self.total = 0
        def BSTsum(node):
            if node is None:
                return None
            BSTsum(node.left)
            self.total += node.val
            BSTsum(node.right)
        BSTsum(root)

        self.prefix = 0
        def helper(node):
            if node is None:
                return None
            helper(node.left)
            self.prefix += node.val
            node.val = self.total - self.prefix + node.val 
            helper(node.right)
        helper(root)
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

root = obj.bstToGst(node)

def show(root, l):
    if root is None:
        return None
    show(root.left, l+1)
    print("     "*l, root.val)
    show(root.right, l+1)

show(root, 0)