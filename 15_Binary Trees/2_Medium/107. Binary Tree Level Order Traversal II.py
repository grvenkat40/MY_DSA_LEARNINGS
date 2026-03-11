from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        res = []
        if root is None:
            return res
        q = deque([root])
        while q:
            l = len(q)
            sub = []
            for i in range(l):
                node = q.popleft()
                sub.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sub)
        rev = res[::-1]
        return rev

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)
node.left.right.left = TreeNode(8)
node.right.left.left = TreeNode(9)
node.right.right.right = TreeNode(10)

obj = Solution()
print(obj.levelOrderBottom(node))