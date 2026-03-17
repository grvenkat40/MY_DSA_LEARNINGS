from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def MYfindBottomLeftValue(self, root) -> int:
        if root is None:
            return None
        arr = []
        q = deque([root])
        while q:
            l = len(q)
            sub = []
            for _ in range(l):
                node = q.popleft()
                sub.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            arr.append(sub)
        return arr[-1][0]
    
    def OptimalfindBottomLeftValue(self, root) -> int:
        if root is None:
            return None
        node = None
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
        return node.val

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

obj = Solution()
print(obj.MYfindBottomLeftValue(root))
print(obj.OptimalfindBottomLeftValue(root))