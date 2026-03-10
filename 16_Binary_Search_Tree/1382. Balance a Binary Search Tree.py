# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root):
        nums = []
        def tree(node):
            if node is None:
                return
            tree(node.left)
            nums.append(node.val)
            tree(node.right)
        tree(root)
        def buildBST(left, right):
            if left > right:
                return
            mid = (left+right) // 2
            value = nums[mid]
            node = TreeNode(value)
            node.left = buildBST(left, mid-1)
            node.right = buildBST(mid+1, right)
            return node
        return buildBST(0, len(nums)-1)
        
node = TreeNode(4)
node.right = TreeNode(1)
node.right.right = TreeNode(2)
node.right.right.right = TreeNode(3)
node.right.right.right.right = TreeNode(4)


obj = Solution()

root = obj.balanceBST(node)

def show(root, l):
    if root is None:
        return None
    show(root.left, l+1)
    print("     "*l, root.val)
    show(root.right, l+1)

show(root, 0)