class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head) :
        hash = {}
        newhead = curr = Node(0)
        
        temp = head
        while temp:
            new_node = Node(temp.val, temp.random)
            curr.next = new_node
            curr = curr.next
            hash[temp] = new_node

        temp = head
        curr = newhead.next
        while temp:
            if temp.random:
                curr.random = hash[temp.random]     
            temp = temp.next
            curr= curr.next
        return newhead.next


head = Node(7)
n2= Node(13)
n3 = Node(11)
n4 = Node(11)
n5 = Node(10)
n6 = Node(1)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

obj = Solution()
print(obj.copyRandomList(head))