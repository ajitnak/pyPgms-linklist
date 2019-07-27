define ll_palindrome(n):
    slow = n
    fast = n
    stack = []
    while fast is not None and fast.get_next() is not None:
        stack.append(slow.get_data())
        slow = slow.get_next()
        fast = fast.get_next().get_next()

    if fast is not None:
        slow = slow.get_next()

    while slow is not None:
        if (slow.get_data() != stack.pop()):
            return False
        slow = slow.get_next()
    return True
