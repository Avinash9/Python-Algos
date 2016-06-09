
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

	# def set_data(self,data):
	# 	self.data = data

	# def get_data(self):
	# 	return self.data

	# def set_next(self,next):
	# 	self.next = next

	# def get_next(self):
	# 	return self.next

	# def has_next(self):
	# 	return self.next != None



class LinkList(object):

	def __init__(self):

		self.length = 0
		self.head = None

	def insert(self,node):
		if self.length == 0:
			self.insert_at_beg(node)
		else:
			self.insert_at_end(node)


	def insert_at_beg(self,node):
		new_node = node
		new_node.next = self.head
		self.head = new_node
		self.length += 1

	def print_link_list(self):
		link_list=[]
		current_node = self.head
		while current_node != None:
			link_list.append(current_node.data)
			current_node = current_node.next
		return link_list

	def insert_at_end(self,node):
		current_node = self.head

		while current_node.next != None:
			current_node = current_node.next

		current_node.next = node
		node.next = None
		self.length += 1

	def insert_at_position(self,node,position):
		current_node = self.head

		pos = 1
		if position > self.length or pos < 0:
			print "The position does not exist. Please enter a valid position"
		else:
			while pos < position-1 and current_node.next != None:
				pos = pos + 1
				current_node = current_node.next

			temp = current_node.next
			current_node.next = node
			node.next = temp
			self.length += 1


	def getLength(self):
		return self.length






node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
node4 = Node(10)
node5 = Node(20)
node6 = Node(30)
l = LinkList()
l.insert(node1)
l.insert(node2)
l.insert(node3)
l.insert(node4)
l.insert(node5)
l.insert(node6)
print l.print_link_list()
print ":::::length of link list:::::",l.getLength()
print "############################"
node7 = Node(60)
l.insert_at_position(node7,50)
print l.print_link_list()








	




