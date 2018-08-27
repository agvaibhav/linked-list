class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        node1 = Node(new_data)
        node1.next = self.head

        temp = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = node1

        else:
            node1.next = node1  #for first node

        self.head = node1

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
cll.printlist()
