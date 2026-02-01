import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to merge k sorted linked lists using a min-heap
    def mergeKLists(self, lists):
        # Initialize a min-heap
        min_heap = []

        # Push the head node of each non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Create a dummy node to build the result list
        dummy = ListNode(0)
        tail = dummy

        # While the heap is not empty
        while min_heap:
            # Extract the node with the smallest value
            val, i, node = heapq.heappop(min_heap)

            # Add it to the result list
            tail.next = node
            tail = tail.next

            # If there's a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # Return the head of the merged list
        return dummy.next

# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Creating three linked lists:
    # list1: 1 -> 4 -> 5
    # list2: 1 -> 3 -> 4
    # list3: 2 -> 6

    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    result = sol.mergeKLists(lists)

    # Print the merged list
    while result:
        print(result.val, end=" ")
        result = result.next
