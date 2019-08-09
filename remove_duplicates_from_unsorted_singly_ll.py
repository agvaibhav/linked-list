def removeDuplicates(head):
    #code here
    temp = head
    while temp is not None:
        last = temp
        temp_new = temp.next
        while temp_new is not None:
            if temp.data== temp_new.data:
                last.next = temp_new.next
                temp_new = temp_new.next
            else:
                last = temp_new
                temp_new = temp_new.next
        temp=temp.next
    return head
