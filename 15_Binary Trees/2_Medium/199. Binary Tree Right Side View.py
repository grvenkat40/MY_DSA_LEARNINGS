from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class MYSolution:
    def rightSideView(self, root):
        ans = []
        if root is None:
            return ans
        hash = {}
        q = deque([(root, 0)])
        while q:
            level = []
            for _ in range(len(q)):
                node, line = q.popleft()
                #if i == size -1:
                #   ans.append(node.val)
                level.append((node, line))
                if node.left:
                    q.append((node.left, line-1))
                if node.right:
                    q.append((node.right, line+1))
            level.sort(key=lambda x:x[1], reverse = True)
            ans.append(level[0][0].val)
        return ans

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(6)
node.right.right = TreeNode(7)

obj = MYSolution()
print(obj.rightSideView(node))