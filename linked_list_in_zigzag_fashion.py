'''
ques

Given a Linked list, rearrange it such that converted list should be of the
form a < b > c < d > e < f .. where a, b, c are consecutive data node
of linked list and such that the order of linked list is sustained.
'''


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

def zigzag(head):
    if head is None or head.next is None:
        return head
    a = head.data
    b = head.next.data
    head.data = min(a,b)
    head.next.data = max(a,b)
    if head.next.next:
        if head.next.data < head.next.next.data:
            head.next.data, head.next.next.data = head.next.next.data, head.next.data
        
    head.next.next = zigzag(head.next.next)
    return head

if __name__=='__main__':

    llist = LinkedList()

    llist.append(11)
    llist.append(15)
    llist.append(20)
    llist.append(5)
    llist.append(10)
    
    print("Original linked list is: ")
    llist.printlist()

    zigzag(llist.head)

    print('zigzag linked list is: ')
    llist.printlist()
