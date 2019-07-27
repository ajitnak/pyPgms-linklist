from sets import Set
from node import Node

define kth_last(n, k):
    if k < 0:
        return None
    p1 = n
    p2 = n

    for i in range (0, k):
        p1 = p1.get_next()

    while p1:
        p1 = p1.get_next()
        p2 = p2.get_next()
    return p2
            
    

