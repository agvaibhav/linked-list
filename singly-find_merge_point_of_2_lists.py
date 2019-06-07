# Python3 program merge two sorted linked
# in third linked list using recursive.
 
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Constructor to initialize the node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Method to print linked list
    def printList(self):
        temp = self.head
         
        while temp :
            print(temp.data, end="->")
            temp = temp.next
 
    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)
         
        if self.head is None:
            self.head = new_node
            return
        last = self.head
         
        while last.next:
            last = last.next
        last.next = new_node
 
 
def findMergeNode(head1, head2):
    curra = head1
    currb = head2

    #Do till the two nodes are the same
    while curra != currb:

    #If you reached the end of one list start at the beginning of the other one

        #currentA
        if(curra.next == None):
            curra = head2
        else:
            curra = curra.next
    
        #currentB
        if(currb.next == None):
            currb = head1;
        else:
            currb = currb.next
    
    return currb.data
 
# Driver Function
if __name__ == '__main__':
        index = int(input("index in list1 where node is merging: "))

        llist1_count = int(input("no of elements in list 1: "))

        llist1 = LinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input("elements of list 1: "))
            llist1.append(llist1_item)
            
        llist2_count = int(input("no of elements in list2: "))

        llist2 = LinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input("elements of list2: "))
            llist2.append(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)
        print(result)
