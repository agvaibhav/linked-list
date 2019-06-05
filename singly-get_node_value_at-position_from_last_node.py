 
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
 
def getNode(head, positionFromTail):
    trailingNode = head
    len = 0
    while(head):
        if len>positionFromTail:
            trailingNode = trailingNode.next
        
        len+=1
        head = head.next
    return trailingNode.data


# Driver Function
if __name__ == '__main__':
 
    
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    ans = getNode(list1.head, 3)
    print(ans)
