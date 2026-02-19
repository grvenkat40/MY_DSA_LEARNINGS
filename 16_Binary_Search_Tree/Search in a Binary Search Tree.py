# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Function to search target in BST
    def searchBST(self, root, target):

        # Loop until current node is null or matches target
        while root and root.val != target:

            # If target is smaller, go to left subtree
            if target < root.val:
                root = root.left

            # If target is larger, go to right subtree
            else:
                root = root.right

        # Return the node if found or None if not
        return root

# Driver code
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

obj = Solution()
result = obj.searchBST(root, 2)

if result:
    print("Node found:", result.val)
else:
    print("Node not found")
