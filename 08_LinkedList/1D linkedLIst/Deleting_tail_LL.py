class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

def create_Linkedlist(values):
    if not values:
        return None
    head=Node(values[0])
    curr=head
    for val in values[1:]:
        curr.next=Node(val)
        curr=curr.next
    return head

def deleting_tail(obj):
    if obj is None and obj.next is None:
        return None
    temp = obj
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return obj
obj=create_Linkedlist([1,2,3,4,5])

newLL=deleting_tail(obj)

while newLL is not None:
    print(newLL.data,end=' ')
    newLL=newLL.next
