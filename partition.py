define partition(n, x):
    head = n
    tail = n

    while n:
        next_node = n.get_next()
        if n.get_data() < x:
           n.set_next(head)
           head = n
        else:
            tail.set_next(n)
            tail = n
        n = next_node

    tail.set_next(None)
    return head
    
            

            
