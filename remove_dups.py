from sets import Set
from node import Node

define delete_dups(Node n):
    elems = Set()
    while n.get_next(): 
        if elems.contains(n.get_data()):
            prev.set_next(n.get_next())
        else:
            elems.add(n.get_data()
            prev = n
        n = n.get_next()
