# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        if not nums:
            return None
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid-1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums)-1) 

obj = Solution()
nums = [-10,-3,0,5,9]
nodes = obj.sortedArrayToBST(nums)

def show(node, l):
    if node is None:
        return None
    show(node.left, l+1)
    print("-->"*l, node.val)
    show(node.right, l+1)

show(nodes, 0)