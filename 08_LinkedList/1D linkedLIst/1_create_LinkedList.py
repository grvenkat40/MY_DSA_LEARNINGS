class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj=Node(1)
obj.next=Node(2)
obj.next.next=Node(3)
obj.next.next.next=Node(4)
obj.next.next.next.next=Node(5)

while obj is not None:
    print(obj.data,end=' ')
    if obj.next is not None:
        print("->",end=' ')
    obj=obj.next
