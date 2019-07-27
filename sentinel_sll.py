import Node from node

class UnorderedList:
    def __init__(self):
        self.sentinel = SentinelNode(None)
        self.sentinel.set_next(self.sentinel)

    def is_empty(self):
        return self.sentinel.get_next() == self.sentinel

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        rerurn self.sentinel.count
        
    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
        return False

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current->get_data() == item:
                found = True
            else:
                prev = current
                current = current->next
        if found:
            if previous:
                previous.set_next(current.get_next())
            else:
                self.head = current.get_next()
