class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


obj=Node(2)
obj.next=Node(3)
obj.next.next=Node(4)
obj.next.next.next=Node(5)

while obj is not None:
    print(obj.data,end=' ')
    if obj.next is not None:
        print("->",end=' ')
    obj=obj.next

print()

class InsertClass:
    def __init__(self,value):
        self.value=value
        self.next=None

obj2=InsertClass(2)
obj2.next=InsertClass(3)
obj2.next.next=InsertClass(4)
obj2.next.next.next=InsertClass(5)

def insert_data(obj2):
    newList=InsertClass(1)
    newList.next=obj2
    return newList

obj2=insert_data(obj2)
while obj2 is not None:
    print(obj2.value,end=' ')
    if obj2.next is not None:
        print("->",end=' ')
    obj2=obj2.next
