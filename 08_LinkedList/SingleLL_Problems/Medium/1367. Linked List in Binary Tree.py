# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head, root) -> bool:
        if root is None:
            return False
        if self.LLinRoot(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def LLinRoot(self, headNode, rootNode):
        if not headNode:
            return True
        if not rootNode:
            return False
        if rootNode.val != headNode.val:
            return False
        return self.LLinRoot(headNode.next, rootNode.left) or self.LLinRoot(headNode.next, rootNode.right)


def build_linked_list(arr) :
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def build_tree(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

# --- Running the Test ---
head_vals = [4, 2, 8]
root_vals = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]

head_node = build_linked_list(head_vals)
root_node = build_tree(root_vals)

sol = Solution()
print(f"Result: {sol.isSubPath(head_node, root_node)}")