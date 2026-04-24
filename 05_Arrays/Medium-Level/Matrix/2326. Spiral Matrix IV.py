class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        matrix = [[-1]*n for _ in range(m)]

        top, bottom = 0, m-1
        left, right = 0, n-1

        curr = head

        while curr:
            for i in range(left, right+1):
                if not curr:
                    return matrix
                matrix[top][i] = curr.val
                curr = curr.next
            top += 1

            for i in range(top, bottom+1):
                if not curr:
                    return matrix
                matrix[i][right] = curr.val
                curr = curr.next
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    if not curr:
                        return matrix
                    matrix[bottom][i] = curr.val
                    curr = curr.next
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    if not curr:
                        return matrix
                    matrix[i][left] = curr.val
                    curr = curr.next
                left += 1

        return matrix


obj = Solution()
m = 3
n = 5
arr = [3,0,2,6,8,1,7,9,4,2,5,5,0]

dummy = ListNode(0)
curr = dummy
for val in arr:
    curr.next = ListNode(val)
    curr = curr.next

head = dummy.next

result = obj.spiralMatrix(m, n, head)

for row in result:
    print(row)