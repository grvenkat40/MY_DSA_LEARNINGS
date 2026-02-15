from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        ans = 0
        if root is None:
            return 0
        q = deque([(root, 0)])
        while q:
            size = len(q)
            _, f_indx = q[0]
            _, l_indx = q[-1]
            ans = max(ans, l_indx - f_indx+1)
            for _ in range(size):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2*i))
                if node.right:
                    q.append((node.right, 2*i+1))
        return ans

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.right.left = TreeNode(5)

obj = Solution()
print(obj.widthOfBinaryTree(node))