# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]):
        if inorder is None or postorder is None or len(inorder) != len(postorder):
            return None
        hash = {val:i for i, val in enumerate(inorder)}
        return self.buildBT(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, hash)
    
    def buildBT(self, inorder, inst, inend, postorder, pst, pend, hash):
        if inst > inend or pst > pend:
            return None
        
        root_val = postorder[pend]
        root = TreeNode(root_val)
        root_inx = hash[root_val]
        left_size = root_inx - inst
        root.left = self.buildBT(inorder, inst, root_inx-1, postorder,pst , pst + left_size-1, hash)
        root.right = self.buildBT(inorder, root_inx+1, inend, postorder, pst+left_size, pend-1, hash)
        return root

obj = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
def printroot(node):
    ans = []
    if node:
        printroot(node.left)
        print(node.val)
        printroot(node.right)

node = obj.buildTree(inorder, postorder)
printroot(node)