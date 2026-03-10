# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root):
        self.arr = []
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        inorder(root)
        dummy = TreeNode(0)
        curr = dummy
        for n in self.arr:
            curr.right = TreeNode(n)
            curr = curr.right
        return dummy.right
        
node = TreeNode(4)
node.left = TreeNode(1)
node.left.left = TreeNode(0)
node.left.right = TreeNode(2)
node.left.right.right = TreeNode(3)
node.right = TreeNode(6)
node.right.left = TreeNode(5)
node.right.right = TreeNode(7)
node.right.right.left = TreeNode(8)

obj = Solution()

root = obj.increasingBST(node)

def show(root, l):
    if root is None:
        return None
    show(root.left, l+1)
    print("     "*l, root.val)
    show(root.right, l+1)

show(root, 0)
        