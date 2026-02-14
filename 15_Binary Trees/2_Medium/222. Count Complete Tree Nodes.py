# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root):
        # ans = []
        # def count(node):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        #     ans.append(node.val)
        #     count(node.left)
        #     count(node.right)
        # count(root)
        # return len(ans)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)

obj = Solution()

print(obj.countNodes(node))