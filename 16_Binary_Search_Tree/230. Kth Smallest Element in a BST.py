# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        ans = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        ans.sort()
        return ans[k-1]
    
node = TreeNode(3)
node.left = TreeNode(1)
node.right = TreeNode(4)
node.left.right = TreeNode(2)

obj = Solution()
print(obj.kthSmallest(node, 3))