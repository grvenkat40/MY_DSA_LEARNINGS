# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Function to search target in BST
    def floor(self, root, target):
        ans = 0
        while root:
            if root.val == target:
                return target
            if root.val < target:
                ans = root.val
                root = root.right
            else:
                root = root.left
        return ans
    
    def ceil(self, root, key):
        ans = -1
        while root:
            if root.val == key:
                return root.val
            if root.val > key:
                ans = root.val
                root  = root.left
            else:
                root = root.right
# Driver code
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Function to search target in BST
    def floor(self, root, target):
        ans = 0
        while root:
            if root.val == target:
                return target
            if root.val < target:
                ans = root.val
                root = root.right
            else:
                root = root.left
        return ans
    
    def ceil(self, root, key):
        ans = -1
        while root:
            if root.val == key:
                return root.val
            if root.val > key:
                ans = root.val
                root  = root.left
            else:
                root = root.right
            return ans
# Driver code
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

# Testing with the value 7
obj = Solution()
val = 7

f_result = obj.floor(root, val)
c_result = obj.ceil(root, val)

print(f"For target {val}:")
print("Floor is:", f_result)
print("Ceil is:", c_result)