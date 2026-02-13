from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def BottomView(self, root):
        ans = []
        if root is None:
            return ans
        hash = {}
        q = deque([(root, 0)])
        while q:
            node, line = q.popleft()
            if node.left:
                q.append((node.left, line-1))
            if node.right:
                q.append((node.right, line+1))
            hash[line] = node.val
        for key in hash:
            ans.append(hash[key])
        return ans

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(6)
node.right.right = TreeNode(7)


obj = Solution()
print(obj.BottomView(node))