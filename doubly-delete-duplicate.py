class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def delete_duplicate(self):

        first = self.head
        temp = self.head
        while first.next.next!=None:
            while temp.next!=None:
                temp=temp.next
                if first.data == temp.data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
            first = first.next
            temp = first

    def printlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next
        print()


dll=DoublyLinkedList()
dll.push(12)
dll.push(11)
dll.push(10)
dll.push(9)
dll.push(9)
dll.push(8)
dll.push(7)
dll.push(10)
dll.push(6)
dll.push(9)
dll.push(5)
dll.push(5)
dll.push(4)
dll.push(3)
dll.push(3)
dll.push(2)
dll.push(2)
dll.push(1)
dll.push(1)
print("linked list before deletionn is:")
dll.printlist()
dll.delete_duplicate()
print("linked list after deletion is:")
dll.printlist()

    
