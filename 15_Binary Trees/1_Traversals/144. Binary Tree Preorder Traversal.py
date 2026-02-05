class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        result = []
        def preorder(node):
            if not node:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result

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
print(obj.preorderTraversal(node))