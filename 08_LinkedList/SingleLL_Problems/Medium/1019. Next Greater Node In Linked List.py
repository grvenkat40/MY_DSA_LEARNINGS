# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head) -> list[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        stack = []
        res = [0] * len(values)
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                idx = stack.pop()
                res[idx] = val
            stack.append(i)
        return res

def buildLL(arr):
    if not arr:
        return None
    node = ListNode(arr[0])
    curr = node
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return node

ll = buildLL([2,7,4,3,5])

obj = Solution()
print(obj.nextLargerNodes(ll))