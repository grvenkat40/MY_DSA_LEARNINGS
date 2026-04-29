# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        before = ListNode(0)
        after = ListNode(0)

        before_pt = before
        after_pt = after

        curr = head
        while curr:
            if curr.val < x:
                before_pt.next = curr
                before_pt = before_pt.next
            else:
                after_pt.next = curr
                after_pt = after_pt.next
            curr = curr.next

        after_pt.next = None
        before_pt.next = after.next
        return before.next

arr = [1,4,3,2,5,2]
x = 3

dummy = ListNode(0)
curr = dummy
for n in arr:
    node = ListNode(n)
    curr.next = node
    curr = curr.next    

obj = Solution()
new = obj.partition(dummy.next, x)
curr = new
while curr:
    print(curr.val, "->", end=" ")
    curr = curr.next 
