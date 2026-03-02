import time
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
class Solution:
    def Brute_Sol_recoverTree(self, root):
        ans = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        ans.sort()
        self.i = 0
        def helper(root):
            if root is None:
                return
            helper(root.left)
            root.val = ans[self.i]
            self.i += 1
            helper(root.right)
        helper(root)
        return root

    def Optimal_Sol_recoverTree(self, root):
        self.first = self.middle = self.last = None
        self.prev = TreeNode(float("-inf"))

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.prev and root.val < self.prev.val:
                if self.first is None:
                    self.first = self.prev
                    self.middle = root
                else:
                    self.last = root
            self.prev = root
            inorder(root.right)
        
        inorder(root)
        if self.first and self.last:
            self.first, self.last = self.last, self.first
        elif self.first  and self.middle:
            self.first, self.middle  = self.middle, self.first
        return root

    
node = TreeNode(1)
node.left = TreeNode(3)
node.left.right = TreeNode(2)

obj = Solution()

def print_tree(root, l):
    if root is None:
        return
    print_tree(root.left, l+1)
    print("      "*l,root.val)
    print_tree(root.right, l+1)

brute_st = time.perf_counter()
root = obj.Brute_Sol_recoverTree(node)
print_tree(root, 0)
brute_end = time.perf_counter()
print("Brute Solution ", brute_end-brute_st)

opti_st = time.perf_counter()
root = obj.Optimal_Sol_recoverTree(node)
print_tree(root, 0)
opti_end = time.perf_counter()
print("Optimal Solution ", opti_end-opti_st)
