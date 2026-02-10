# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        def maxPath(node):
            if node is None:
                return 0
            LHS = maxPath(node.left)
            RHS = maxPath(node.right)
            if LHS < 0:
                LHS = 0
            if RHS < 0:
                RHS = 0
            self.maxSum = max(self.maxSum, LHS+RHS+node.val)
            return node.val + max(LHS, RHS)
        maxPath(root)
        return self.maxSum

node = TreeNode(-10)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

# node = TreeNode(2)
# node.left = TreeNode(-1)
# node.right = TreeNode(20)



obj = Solution()
print("Max Path Sum: ",obj.maxPathSum(node))