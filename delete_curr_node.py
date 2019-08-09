def deleteNode(curr_node):
    #code here
    if curr_node is None:
        return
    if curr_node.next is None:
        return
    curr_node.data = curr_node.next.data
    curr_node.next = curr_node.next.next
