# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = dummy.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next


head = ListNode(7)
n2= ListNode(13)
n3 = ListNode(11)
n4 = ListNode(11)
n5 = ListNode(10)
n6 = ListNode(1)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
obj = Solution()

nodes = obj.removeElements(head, 11)

while nodes:
    print(nodes.val, "->", end=' ')
    nodes = nodes.next