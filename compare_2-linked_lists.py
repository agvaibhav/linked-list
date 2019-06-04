 
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
 
def compare_lists(llist1, llist2):
    if llist1 is None and llist2 is not None:
        return 0
    elif llist2 is None and llist1 is not None:
        return 0
    elif llist1 is None and llist2 is None:
        return 1
    else:
        if llist1.data == llist2.data:
            res = compare_lists(llist1.next,llist2.next)
            if res==1:
                return 1
            else:
                return 0
        else:
            return 0


# Driver Function
if __name__ == '__main__':
 
    
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)
 
    
    list2 = LinkedList()
    list2.append(10)
    list2.append(20)
    list2.append(30)
    list2.append(40)
    list2.append(50)

    ans = compare_lists(list1.head, list2.head)
    if ans == 1:
        print("the 2 given linked lists are same")
    else:
        print("the 2 given linked lists are not same")
