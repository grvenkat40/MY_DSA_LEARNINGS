from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def markParent(self, root, track_parent, target):
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                track_parent[node.left] = node
                q.append(node.left)
            if node.right:
                track_parent[node.right] = node
                q.append(node.right)
             
    def distanceK(self, root, target, k: int):
        track_parent = {}
        self.markParent(root, track_parent, target)
        visited = {}
        qu = deque([target])
        visited[target] = True
        curr_lvl = 0
        while qu:
            size = len(qu)
            if curr_lvl == k:
                break
            curr_lvl += 1
            for i in range(size):
                node = qu.popleft()
                if node.left and visited.get(node.left) is None:
                    qu.append(node.left)
                    visited[node.left] = True
                if node.right and visited.get(node.right) is None:
                    qu.append(node.right)
                    visited[node.right] = True
                if track_parent.get(node) and visited.get(track_parent[node]) is None:
                    qu.append(track_parent.get(node))
                    visited[track_parent[node]] = True
        result = []
        while qu:
            curr = qu.popleft()
            result.append(curr.val)
        return result

node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)

obj = Solution()
print(obj.distanceK(node, node.left, 2))