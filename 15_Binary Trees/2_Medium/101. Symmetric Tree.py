from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        q = deque([root])
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            i = 0
            j = len(level) -1
            while i<=j:
                if level[i] == level[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        return True
                
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)

obj = Solution()

print(obj.isSymmetric(node))
