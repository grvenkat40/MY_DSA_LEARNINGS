class InsertClass:
    def __init__(self,value):
        self.value=value
        self.next=None

def creating_linkedList(values):
    head=InsertClass(values[0])
    curr=head
    for val in values[1:]:
        curr.next=InsertClass(val)
        curr=curr.next
    return head

def insert_at_end(LL,data):
    temp = LL
    while temp.next is not None:
        temp =temp.next
    new_node=InsertClass(6)
    temp.next= new_node
    return LL

LL=creating_linkedList([1,2,3,4,5])

data=6
new_list=insert_at_end(LL,data)

while new_list:
    print(new_list.value,end=' ')
    new_list=new_list.next


