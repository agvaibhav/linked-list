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

def pairWiseSwap(head):
    # code here
    if head is None:
        return
    temp = head
    while temp and temp.next:
        first = temp.data
        second = temp.next.data
        temp.data = second
        temp.next.data = first
        temp = temp.next.next
#    return head


if __name__=='__main__':

    llist = LinkedList()

    llist.append(6)

    llist.push(7)

    llist.push(1)

    llist.append(4)

    llist.insertAfter(llist.head.next, 8)
    n = 5
    print("Original linked list is: ")
    llist.printlist()
    pairWiseSwap(llist.head)
    print('new linked list is: ')
    llist.printlist()
