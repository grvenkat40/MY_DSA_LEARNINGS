# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        before = dummy
        for _ in range(left-1):
            before = before.next
        prev = None
        curr = before.next
        for _ in range(right-left + 1):
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        before.next.next = curr
        before.next = prev
        return dummy.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)


obj = Solution()
res = obj.reverseBetween(node, 2, 4)

while res:
    print(res.val, "->", end=' ')
    res = res.next