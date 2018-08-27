import gc
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        temp=self.head
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node

    def delete(self, key):
        temp = self.head

        if temp is None:
            return

        if(temp.data == key):
            
            while(temp.next != self.head):
                temp=temp.next
            temp.next = self.head.next

            self.head = self.head.next
            return
        
        while(temp is not None):
            if(temp.next.data == key):
                break
            temp = temp.next

        next = temp.next.next
        temp.next = next

        gc.collect()

    def printlist(self):
        temp = self.head
        while(self.head is not None):
            print(temp.data)
            temp = temp.next
            if(temp == self.head):
                break

cll = CircularLinkedList()
cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
print("created linked list is:")
cll.printlist()
cll.delete(3)
print("modified linked list is:")
cll.printlist()
