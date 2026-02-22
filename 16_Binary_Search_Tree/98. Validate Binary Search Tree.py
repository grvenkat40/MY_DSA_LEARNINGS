
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        minVal = float('-inf')
        maxVal = float('inf')
        return self.ValiedBST(root, minVal, maxVal)
    
    def ValiedBST(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        
        return self.ValiedBST(root.left, minVal, root.val) and self.ValiedBST(root.right, root.val, maxVal)
    

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.left.left = TreeNode(7)
# root.left.right = TreeNode(12)
# root.left.left.right = TreeNode(9)
# root.left.left.right.left = TreeNode(8)
# root.right.left = TreeNode(14)
# root.right.right = TreeNode(17)
# root.right.right.left = TreeNode(18)

obj = Solution()
print(obj.isValidBST(root))