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

obj=create_Linkedlist([1,2,3,4,5])

cnt=0
while obj is not None:
    obj=obj.next
    cnt+=1
print(cnt)
