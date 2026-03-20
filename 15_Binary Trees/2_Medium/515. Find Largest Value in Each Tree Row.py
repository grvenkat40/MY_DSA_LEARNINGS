from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            l = len(q)
            maxi = float('-inf')
            for _ in range(l):
                node = q.popleft()
                maxi = max(maxi, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxi)
        return res

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(6)
node.right.right = TreeNode(7)

obj = Solution()
print(obj.largestValues(node))