# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        def ArrToBST(left, right):
            if left > right:
                return None
            mid = (left+right) // 2
            node = TreeNode(nums[mid])
            node.left = ArrToBST(left, mid-1)
            node.right = ArrToBST(mid+1, right)
            return node
        return ArrToBST(0, len(nums)-1)
 

obj = Solution()
# nums = [-10,-3,0,5,9]
L = ListNode(-10)
L.next = ListNode(-3)
L.next.next = ListNode(0)
L.next.next.next = ListNode(5)
L.next.next.next.next = ListNode(9)

nodes = obj.sortedListToBST(L)

def show(node, l):
    if node is None:
        return None
    show(node.left, l+1)
    print("     "*l, node.val)
    show(node.right, l+1)

show(nodes, 0)