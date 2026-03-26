# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        if head is None:
            return
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        hash = {}
        curr = dummy
        while curr:
            prefix_sum += curr.val
            hash[prefix_sum] = curr
            curr = curr.next
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = hash[prefix_sum].next
            curr = curr.next
        return dummy.next

arr = [1,2,-3,3,1]
head = ListNode(arr[0])
for val in arr[1:]:
    node = ListNode(val)
    head.next = node
    head = head.next

obj = Solution()
res = obj.removeZeroSumSublists(head)

while res:
    print(res.val,'->')
    res = res.next
