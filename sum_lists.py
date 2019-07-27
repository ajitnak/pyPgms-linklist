define sum_lists(n1, n2, c):
    if n1 is None and n2 is None and c == 0 :
        return None
   
    val = c 
    result = Node()
    if n1 is not None:
        val = result.data + n1.get_data()

    if n2 is not None:
        val = result.data + n2.get_data()

    result.set_daa(val % 10)

    if n1 is not None or n2 is not None:
        next_n1 = None
        next_n2 = None
        carry = 0
        if n1 is not None:
            next_n1 = n1.get_next()
        if n1 is not None:
            next_n2 = n2.get_next()
        if val >= 10:
            carry = 1
        
        
        more = sum_lists(next_n1, next_n2, carry)

        result.set_next(more)
    return result

    
    
    
    
