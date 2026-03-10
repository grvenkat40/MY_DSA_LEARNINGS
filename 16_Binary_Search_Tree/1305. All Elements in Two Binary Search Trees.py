# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1, root2) -> list[int]:
        arr = []
        def first_tree(node):
            if node is None:
                return
            first_tree(node.left)
            arr.append(node.val)
            first_tree(node.right)
        first_tree(root1)
        def second_tree(node):
            if node is None:
                return
            second_tree(node.left)
            arr.append(node.val)
            second_tree(node.right)
        second_tree(root2)
        arr.sort()
        return arr
    
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

obj = Solution()

ans = obj.getAllElements(root1, root2)

print(ans)