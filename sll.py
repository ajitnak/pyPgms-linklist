import Node from node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current->next
        rerurn count
        
    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
        return False

    def remove(self, item):
        if self.head == None:
            return
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

    def __iter__(self):
        current = self.head
        while current:
            yield current.get_data()
            current = current.get_next()

    def __str__(self):
        print str(list(self))
