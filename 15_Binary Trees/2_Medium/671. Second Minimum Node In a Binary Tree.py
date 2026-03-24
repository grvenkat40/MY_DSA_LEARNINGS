# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        self.min_val = root.val
        self.ans = float('inf')
        def dfs(node):
            if node is None:
                return
            if self.min_val < node.val < self.ans:
                self.ans = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans if self.ans != float('inf') else -1
    
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)

obj = Solution()
print(obj.findSecondMinimumValue(root))