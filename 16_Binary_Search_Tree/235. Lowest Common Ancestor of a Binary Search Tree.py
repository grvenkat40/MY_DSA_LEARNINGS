# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        curr = root.val
        if curr < p.val and curr < q.val:        
            return self.lowestCommonAncestor(root.right, p, q)
        if curr > p.val and curr > q.val:
            self.lowestCommonAncestor(root.left, p, q)
        return root
        
root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

obj = Solution()
p = root.left.right.left
q = root.left.right.right  
print(obj.lowestCommonAncestor(root, p, q).val) # Output: 2