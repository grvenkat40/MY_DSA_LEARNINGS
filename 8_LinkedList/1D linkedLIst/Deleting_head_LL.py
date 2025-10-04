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

def deleting_head(obj):
    if obj is None:
        return None
    return obj.next

obj=create_Linkedlist([1,2,3,4,5])

newLL=deleting_head(obj)

while newLL is not None:
    print(newLL.data,end=' ')
    newLL=newLL.next
