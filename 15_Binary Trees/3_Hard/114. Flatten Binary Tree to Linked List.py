# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        self.prev = None
        def flat(node):
            if node is None:
                return
            flat(node.right)
            flat(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        flat(root)
        return root
    
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(5)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.right = TreeNode(6)
node.right.right.left = TreeNode(7)

obj = Solution()
ans = obj.flatten(node)

def showBT(ans):
    while ans:
        print(ans.val, end=" -> ")
        ans = ans.right
    print(None)
showBT(ans)
