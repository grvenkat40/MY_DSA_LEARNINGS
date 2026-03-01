# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:
        hash = set()
        def helper(root):
            if  root is None:
                return False
            need = k - root.val
            if need in hash:
                return True
            hash.add(root.val)
            return helper(root.left) or helper(root.right)
        return helper(root)
    
node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(6)
node.left.left = TreeNode(2)
node.left.right = TreeNode(4)
node.right.right = TreeNode(7)

obj = Solution()
print(obj.findTarget(node, 9))