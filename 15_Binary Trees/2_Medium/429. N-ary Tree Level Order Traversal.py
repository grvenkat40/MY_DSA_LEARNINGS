from collections import deque
# Definition for a Node.

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    if child:
                        q.append(child)
            res.append(level)
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
print(obj.levelOrder(root))