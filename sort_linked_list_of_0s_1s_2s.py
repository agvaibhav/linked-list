class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("the given previous node is not in given linkedlist")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last=self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()

def segregate(head):
    #code here
    temp = head
    count_0 = 0
    count_1 = 0
    count_2 = 0
    while temp is not None:
        if temp.data == 0:
            count_0 += 1
        elif temp.data == 1:
            count_1 += 1
        elif temp.data ==2:
            count_2 += 1
        temp = temp.next

    while count_0>0:
        head.data = 0
        head = head.next
        count_0 -= 1
    while count_1 > 0:
        head.data = 1
        head = head.next
        count_1 -= 1
    while count_2 > 0:
        head.data = 2
        head = head.next
        count_2 -= 1
    


if __name__=='__main__':

    llist = LinkedList()

    llist.append(1)
    llist.append(2)
    llist.append(0)
    llist.append(2)
    llist.append(1)
    
    print("Original linked list is: ")
    llist.printlist()

    segregate(llist.head)

    print('sorted linked list is: ')
    llist.printlist()
