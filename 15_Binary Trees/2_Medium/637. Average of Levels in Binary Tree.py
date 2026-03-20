from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return None
        q = deque([root])
        res = []
        while q:
            l = len(q)
            add = 0
            for _ in range(l):
                node = q.popleft()
                add += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg = add / l
            res.append(avg)
        return res

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(6)
node.right.right = TreeNode(7)

obj = Solution()
print(obj.averageOfLevels(node))