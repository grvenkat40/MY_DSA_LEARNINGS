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

def search_Ele(obj,Ele):
    while obj is not None:
        if obj.data == Ele:
            return True
        obj=obj.next
    return False

obj=create_Linkedlist([1,2,3,4,5])
Ele=6
print(search_Ele(obj,Ele))