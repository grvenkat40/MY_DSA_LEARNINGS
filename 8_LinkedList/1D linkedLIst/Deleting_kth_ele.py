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

def deleting_kth_ele(obj,k):
    cnt=0
    temp = obj
    prev = None

    while temp:
        if temp is None and temp.next is None:
            return obj
        if temp is not None:
            cnt+=1
            if cnt == k:
                prev.next = prev.next.next
            prev = temp
            temp = temp.next
    return obj


obj=create_Linkedlist([1,2,3,4,5])  # Creating the Linked list

k=3
newLL=deleting_kth_ele(obj,k)  # Deleting the Kth element

while newLL is not None:
    print(newLL.data,end=' ')
    newLL=newLL.next
