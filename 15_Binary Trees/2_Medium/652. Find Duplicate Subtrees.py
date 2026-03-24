# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findDuplicateSubtrees(self, root):
        self.counts = {}
        self.res = []

        def find(node):
            if not node:
                return ""
            serial = f"{node.val},{find(node.left)},{find(node.right)}"
            self.counts[serial] = self.counts.get(serial, 0) + 1
            if self.counts[serial] == 2:
                self.res.append(node)
            return serial
        find(root)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)

obj = Solution()
print(obj.findDuplicateSubtrees(root))