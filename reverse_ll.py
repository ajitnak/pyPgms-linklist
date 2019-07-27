class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
def reverse_ll(Node head):
	prev, curr = None, head
	while curr:
		tmp = curr.next
		curr.next = prev
		prev = curr
		curr = tmp
	return


	
