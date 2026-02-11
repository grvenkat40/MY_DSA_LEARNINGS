from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        q = deque([root])
        left_to_right = True
        if root is None:
            return result
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if left_to_right:
                result.append(level)
            else:
                result.append(level[::-1])
            left_to_right = not left_to_right

        return result

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

obj = Solution()

print(obj.zigzagLevelOrder(node))