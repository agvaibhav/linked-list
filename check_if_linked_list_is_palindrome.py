def isPalindrome(head):
    #code here
    stack = []
    while head is not None:
        stack.append(head.data)
        head = head.next
    for i in range(len(stack)//2):
        if len(stack)>=1:
            if stack[i] == stack.pop():
                continue
            else:
                return False
    return True
