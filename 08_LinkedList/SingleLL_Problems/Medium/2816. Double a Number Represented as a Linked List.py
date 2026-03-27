# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def My_doubleIt(self, head):
        num = ""
        while head:
            num += str(head.val)
            head = head.next
        res = int(num) * 2
        arr = str(res)
        dummy = ListNode(0)
        curr = dummy
        for n in arr:
            node = ListNode(int(n))
            curr.next = node
            curr = node
        return dummy.next   
    
    def Optimal_doubleIt(self, head):
        def reverse(curr):
            prev = None
            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
            return prev
        
        head = reverse(head)
        carry = 0
        curr = head
        while curr:
            total = (curr.val * 2) + carry
            curr.val = total % 10
            carry = total // 10
            if curr.next is None:
                if carry:
                    curr.next = ListNode(carry)
                break
            curr = curr.next
        return reverse(head)

    def OptimalRecursivedoubleIT(self, head):
        def dfs(node):
            if not node:
                return 0  # carry
            
            carry = dfs(node.next)
            
            total = node.val * 2 + carry
            node.val = total % 10
            
            return total // 10  # return carry
        
        carry = dfs(head)
        
        # If extra carry at the front
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        
        return head
    
arr = [1,8,9]

def build_linked_list(arr):
    head = ListNode(arr[0])
    curr = head

    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head

l1 = build_linked_list(arr)


obj = Solution()

head = obj.My_doubleIt(l1)
head2 = obj.Optimal_doubleIt(l1)
head3 = obj.OptimalRecursivedoubleIT(l1)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_list(head)
print_list(head2)
print_list(head3)