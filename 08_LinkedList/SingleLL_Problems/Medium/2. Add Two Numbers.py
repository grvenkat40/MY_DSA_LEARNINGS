# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 is not None or l2 is not None) or carry:
            sum = 0
            if l1 is not None:
                sum+=l1.val
                l1 = l1.next
            if l2 is not None:
                sum+=l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10
            node = ListNode(sum%10)
            temp.next = node
            temp = temp.next
        return dummy.next 
            
def build_linked_list(arr):
    head = ListNode(arr[0])
    curr = head

    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head

l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])

obj = Solution()

head = obj.addTwoNumbers(l1, l2)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_list(head)