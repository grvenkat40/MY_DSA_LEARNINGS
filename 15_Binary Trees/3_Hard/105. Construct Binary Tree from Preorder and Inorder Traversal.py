# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        if preorder is None or inorder is None or len(preorder) != len(inorder):
            return None
        hash = {val:i for i, val in enumerate(inorder)}
        return self.buildBT(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, hash)
    
    def buildBT(self, preorder, pre_st, pre_end, inorder, in_st, in_end, hash):
        if in_st > in_end or pre_st > pre_end:
            return None
        root_val = preorder[pre_st]
        root = TreeNode(root_val)
        root_inx = hash[root_val]
        left_size = root_inx - in_st
        root.left = self.buildBT(preorder, pre_st+1, pre_st + left_size, inorder, in_st, root_inx-1,hash)
        root.right = self.buildBT(preorder, pre_st+left_size+1, pre_end, inorder, root_inx +1, in_end, hash) 
        return root
    
obj = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
def print_tree(node, level=0):
    if node:
        print_tree(node.right, level + 1)
        print("    " * level + str(node.val))
        print_tree(node.left, level + 1)

# Usage:
root = obj.buildTree(preorder, inorder)
print_tree(root)