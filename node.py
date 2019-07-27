class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        return self.next = new_next
    
    def set_data(self, new_data):
        return self.data = new_data

class SentinelNode(Node):
    def __init__(self, data):
        Node.__init__(data)
        self.count = 0
          
    
    

