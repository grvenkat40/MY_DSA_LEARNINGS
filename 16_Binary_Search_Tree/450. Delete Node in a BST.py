# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return self.helper(root)
        dummy = root
        while root:
            if root.val > key:
                if root.left != None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right != None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    def helper(self, root):
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        lastright = self.findLastChild(root.left)
        lastright.right = root.right
        return root.left

    def findLastChild(self, root):
        if root.right == None:
            return root
        return self.findLastChild(root.right)
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

obj = Solution()
print(obj.deleteNode(root, 7))