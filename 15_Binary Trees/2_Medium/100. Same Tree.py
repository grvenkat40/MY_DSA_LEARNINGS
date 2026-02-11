# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class MYSolution:
    def isSameTree(self, p,q):
        result1 = []
        result2 = []

        def tree1(node):
            if node is None:
                result1.append(None)
                return
            result1.append(node.val)
            tree1(node.left)
            tree1(node.right)
        tree1(p)

        def tree2(node):
            if node is None:
                result2.append(None)
                return
            result2.append(node.val)
            tree2(node.left)
            tree2(node.right)
        tree2(q)
        return result1 == result2

class BetterSolution:
    def isSameTree(self, p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

obj = MYSolution()

print(obj.isSameTree(p, q))
#-------------------------------------------

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

obj = BetterSolution()

print(obj.isSameTree(p, q))