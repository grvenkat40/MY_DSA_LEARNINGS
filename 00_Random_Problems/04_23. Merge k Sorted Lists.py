# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode()
        curr = dummy

        for node in lists:
            while node:
                curr.next = node
                node = node.next
                curr = curr.next

        res = []
        curr = dummy.next
        while curr:
            res.append(curr.val)
            curr = curr.next

        res.sort()

        final_ans = ListNode()
        curr = final_ans
        for val in res:
            curr.next = ListNode(val)
            curr = curr.next

        return final_ans.next

def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

lists = [build_linked_list([1,4,5]), build_linked_list([1,3,4]), build_linked_list([2,6])]

obj = Solution()
head = obj.mergeKLists(lists)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
