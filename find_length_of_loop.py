def countNodesinLoop(head):
    #Your code here
    temp = head
    slow = temp.next
    fast = temp.next.next
    for i in range(500):
        if temp.next is None:
            break
        temp = temp.next
    if temp.next is None:
        return 0
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    count = 1
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next
    return count
