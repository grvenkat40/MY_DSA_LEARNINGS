class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def creating_LL(values):
    if not values:
        return None
    head=Node(values[0])
    curr=head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def insert_at_Kth_place(LL,k,value):
    if LL is None:
        new_node=Node(value)
        return new_node
        return LL
    if k==1:
        new = Node(value)
        new.next = LL
        return new
    temp = LL
    cnt=0
    while temp:
        if temp is not None:
            cnt+=1
            if cnt == k-1:
                new_Node=Node(value)
                new_Node.next = temp.next
                temp.next = new_Node
            temp = temp.next
    return LL

LL=creating_LL([1,2,3,4,5,6])

new_LL=insert_at_Kth_place(LL, 7, 10)

while new_LL:
    print(new_LL.data,end=' ')
    new_LL=new_LL.next