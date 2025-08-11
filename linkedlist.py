"""

Dynamic and good for insertions and deletions.
Slower for finding an element at a specific position.

A head node is the first node in a linked list.
A node displays the placement of an item in a list.

code from: https://www.youtube.com/watch?v=rv01fIKIZoU
"""

class Node:
	def __init(self, data, next_note=None):
		self.data = data
		self.next_node = next_node
class LinkedList:
	def __init__():
		self.head = None
		self.last_node = None

	def __repr__(self):
		node  = self.head
		nodes = []
		while node is not None:
			nodes.append(str(node.data))
			node = node.next_node
		nodes.append("None")
		return " -> ".join(nodes)

	def insert_beginning(self, data):
		if self.head is None:
			self.head = Node(data)
			self.last_node = self.head
		else:
			new_node = Node(data, self.head)
			self.head = new_node


	def insert_end(self, data):
		if self.head is None:
			insert_beginning(data)
		else:
			self.last_node.next_node = Node(data)
			self.last_node = self.last_node.next_node			

ll = LinkedList()

ll.insert_beginning(2)
ll.insert_end(1)
ll.insert_end(4)

print(ll)
