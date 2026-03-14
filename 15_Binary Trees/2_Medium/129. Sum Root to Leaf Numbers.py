# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        res = []
        def helper(node, val):
            if node is None:
                return
            val.append(node.val)
            if node.left is None and node.right is None:
                sub = "".join(map(str, val))
                res.append(sub)
            helper(node.left, val)
            helper(node.right, val)
            val.pop()
        helper(root, [])
        total = 0
        for num in res:
            total += int(num)
        return total

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

obj = Solution()
print(obj.sumNumbers(node))