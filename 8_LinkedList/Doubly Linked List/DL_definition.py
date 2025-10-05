class Node:
    def __init__(self,value):
        self.data = value 
        self.prev = None
        self.next = None
    
if __name__ == '__main__':
    head = Node(10)

    head.next = Node(20)
    head.next.prev = head

    head.next.next = Node(30)
    head.next.next.prev = head.next

    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    head.next.next.next.next = Node(50)
    head.next.next.next.next.prev = head.next.next.next

    temp = head

    while temp is not None:
        print(temp.data, end=' ')
        if temp.next is not None:
            print('<->' ,end=' ')
        temp = temp.next