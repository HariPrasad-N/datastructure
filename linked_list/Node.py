class Node:
	def __init__(self,data=None):
		"""
		attributes:
			-> data - data in the node
		"""
		self.data=data
		self.next=None
		self.prev=None

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str(self.data)

	def __add__(self,rnode):
		"""
		adds the data of two Node variables and returns data
		Raises TypeError if type of data attribute does not support substraction
		"""
		return self.data+rnode.data

	def __sub__(self,rnode):
		"""
		substracts the data of two Node variables and returns data
		Raises TypeError if type of data attribute does not support substraction
		"""
		return self.data-rnode.data

	

if __name__ == '__main__':
	node1 = Node(1)
	node2 = Node(2)
	print(node1,'+',node2,'=',node1+node2)
	a=node1-node2
	print(a)
