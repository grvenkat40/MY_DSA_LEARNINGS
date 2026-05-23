# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root) -> str:
        self.res = "~"

        def dfs(node, path):
            if node is None:
                return None
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                curr = "".join(reversed(path)) 
                self.res = min(self.res, curr)

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()
        dfs(root, [])
        return self.res

root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)


arr = [0,1,2,3,4,3,4]

obj = Solution()
print(obj.smallestFromLeaf(root))
