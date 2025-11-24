#Recommend do not run just understand the logic

head = [3,2,0,-4] # Linked list
pos = 1           # where the loop started at 1 index (0-based index)

class Solution:
    def hasCycle(self, head) -> bool:
        hash = {}
        temp = head
        while temp is not None:         #T.C : O(N+log(N)) and S.C : O(N)
            if temp in hash:
                return True
            hash[temp] = hash.get(temp,0)+1
            temp = temp.next
        return False

# Optimal Approach

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head                    #T.C : O(N) and S.C : O(1)             
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False