# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]):
        if preorder is None:
            return None
        inorder = sorted(preorder)
        hash = {val : i for i, val in enumerate(inorder)}
        return self.build(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1, hash)
    def build(self, inorder, in_st, in_end, preorder, pre_st, pre_end, hash):
        if in_st > in_end or pre_st > pre_end:
            return None
        root_val = preorder[pre_st]
        root = TreeNode(root_val)
        root_inx = hash[root_val]
        left_size = root_inx - in_st
        root.left = self.build(inorder, in_st, root_inx-1, preorder, pre_st+1, left_size+pre_st, hash)
        root.right = self.build(inorder, root_inx+1, in_end, preorder, left_size+pre_st+1, pre_end, hash)
        return root
    
preorder = [8,5,1,7,10,12]
obj = Solution()
def printroot(node, l = 0):
    ans = []
    if node:
        printroot(node.left, l + 1)
        print("      "*l+str(node.val))
        printroot(node.right, l + 1)

node = obj.bstFromPreorder(preorder)
printroot(node)