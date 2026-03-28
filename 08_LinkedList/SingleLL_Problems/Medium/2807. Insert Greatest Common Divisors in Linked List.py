# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def GCD(self, a, b):
        while b:
            a, b = b, a%b
        return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return head
        curr = head
        while curr.next:
            value = self.GCD(curr.val, curr.next.val)
            node = ListNode(value)
            node.next = curr.next
            curr.next = node
            curr = node.next
        return head


# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3] 