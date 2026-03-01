class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def SuccBST(self, root, key):
        succ = -1
        while root is not None:
            if root.val > key:
                succ = root.val
                root = root.left
            else:
                root = root.right
        return succ
    
    def PrecBST(self, root, k):
        while root is not None:
            if root.val < k:
                prec = root.val
                root = root.right
            else:
                root = root.left
        return prec
    
node = TreeNode(5)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(4)
node.right = TreeNode(10)
node.right.left = TreeNode(7)
node.right.right = TreeNode(12)

obj = Solution()
print(obj.SuccBST(node, 10))
print(obj.PrecBST(node, 10))