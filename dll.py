class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

class SentinelNode(Node):
    def __init__(self, data):
        super(SentinelNode, self).__init__(data)
        self.count = 0

class DLL:
    def __init__(self):
        self.sentinel = SentinelNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
    
    def first_node(self):
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next

    def size(self):
        return self.sentinel.count

    def insert_after(self, x, item):
        y = Node(item)
        y.prev = x
        y.next = x.next 
        x.next.prev = y
        x.next = y
        
        self.sentinel.count +=1

    def prepend(self, item):
        self.insert_after(self.sentinel, item)

    def append(self, item):
        last_node = self.sentinel.prev
        self.insert_after(last_node, item)

    def find(self, item):
        self.sentinel.data = item
       
        x = self.first_node()
        while x.data != item:
            x = x.next

        self.sentinel.data = None

        if x == self.sentinel:
            return None

        return x

    def delete(self, x):
        if not x:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.sentinel.count -= 1

    def __str__(self):
        s = "["
        x = self.sentinel.next
        while x != self.sentinel:
            if type(x.data) == str:
                s += "'"
            s += str(x.data)
            if x.next != self.sentinel:
                s += ", "
            x = x.next
        s += "]"
        return s

l = DLL()
l.append("Maine")
l.append("Idaho")
l.append("Utah")
node = l.find("Idaho")
print "node: {}".format(node)
if node != None:
        print(node.get_data())
        l.insert_after(node, "Ohio")
print(l)
print "size of list {}".format(l.size())

# Delete Idaho.
if node != None:
    l.delete(node)
print(l)
print "size of list {}".format(l.size())

# Empty out the list, one node at a time.
while l.first_node() != None:
    l.delete(l.first_node())

print(l)
print "size of list {}".format(l.size())
