# Definition for a Node.
class Node:
    def __init__(self, val = None, children  = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return []
        res = []
        def helper(node):
            if node is None:
                return
            if node.children:
                for child in node.children:
                    helper(child)
            res.append(node.val)
        helper(root)
        return res

node5 = Node(5)
node6 = Node(6)
node2 = Node(2)
node4 = Node(4)

# Node 3 with children 5 and 6
node3 = Node(3, [node5, node6])

# Root node 1 with children 3, 2, 4
root = Node(1, [node3, node2, node4])

obj = Solution()
print(obj.postorder(root))