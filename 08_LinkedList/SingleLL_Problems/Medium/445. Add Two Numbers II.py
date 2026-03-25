# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while st1 or st2 or carry:
            v1 = st1.pop() if st1 else 0
            v2 = st2.pop() if st2 else 0
            total = (v1 + v2 + carry)
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head
            head = node
        return head
            
def build_linked_list(arr):
    head = ListNode(arr[0])
    curr = head

    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head

l1 = build_linked_list([7,2,4,3])
l2 = build_linked_list([5,6,4])

obj = Solution()

head = obj.addTwoNumbers(l1, l2)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_list(head)