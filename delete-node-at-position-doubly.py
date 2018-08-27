import gc
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node

    def delete(self, position):
        if self.head == None:
            return

        temp = self.head
        
        if(position==0):
            self.head = temp.next
            temp.next.prev=None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        
        temp.next = next
        next.prev = temp

        gc.collect()

    def printlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next

dll=DoublyLinkedList()
dll.push(4)
dll.push(3)
dll.push(2)
dll.push(1)
print("created linked list is :")
dll.printlist()
dll.delete(2)
print("modified linked list is:")
dll.printlist()
