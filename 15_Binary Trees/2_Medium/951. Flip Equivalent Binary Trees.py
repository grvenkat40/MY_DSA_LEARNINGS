# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return no_flip or flip
            
# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)

root1.right.right = TreeNode(6)


# Tree 2
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)

root2.left.right = TreeNode(6)

root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)

root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)


obj = Solution()
print(obj.flipEquiv(root1, root2))