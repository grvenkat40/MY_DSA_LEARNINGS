from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root is None:
            return None
        q = deque([root])
        while q:
            l = len(q)
            prev = None
            for i in range(l):
                curr = q.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            curr.next = None
        return root

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)

obj = Solution()
def printroot(root, l = 0):
    ans = []
    if root:
        printroot(root.left, l + 1)
        print("      "*l+str(node.val))
        printroot(root.right, l + 1)

root = obj.connect(node)
printroot(root)