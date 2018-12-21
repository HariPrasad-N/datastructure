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

	def	__neg__(self):
		"""
		returns negation(a.data) for a Node
		Raises TypeError if type of data attribute does not support negation
		"""
		return self.data*-1

	def __add__(self,rnode):
		"""
		returns a.data+b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support addition
		"""
		return self.data+rnode.data

	def __sub__(self,rnode):
		"""
		returns a.data-b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support substraction
		"""
		return self.data-rnode.data

	def __mul__(self,rnode):
		"""
		returns a.data*b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support multiplication
		"""
		return self.data*rnode.data


	def	__floordiv__(self,rnode):
		"""
		returns a.data//b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support floor division
		"""
		return self.data//rnode.data

	def	__truediv__(self,rnode):
		"""
		returns a.data/b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support division
		"""
		return self.data/rnode.data

	def __lt__(self,rnode):
		"""
		returns a.data<b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support logical operations
		"""
		return self.data < rnode.data

	def __le__(self,rnode):
		"""
		returns a.data<=b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support logical operations
		"""
		return self.data <= rnode.data 

	# def __eq__(self,rnode):
	# 	"""
	# 	returns a.data==b.data for a and b Nodes
	# 	Raises TypeError if type of data attribute does not support logical operations
	# 	"""
	# 	if rnode is not None:
	# 		return self.data == rnode.data
	# 	else:
	# 		return False

	# def __ne__(self,rnode):
	# 	"""
	# 	returns a.data!=b.data for a and b Nodes
	# 	Raises TypeError if type of data attribute does not support logical operations
	# 	"""
	# 	return self.data != rnode.data

	def __ge__(self,rnode):
		"""
		returns a.data>=b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support logical operations
		"""
		return self.data >= rnode.data

	def __gt__(self,rnode):
		"""
		returns a.data>b.data for a and b Nodes
		Raises TypeError if type of data attribute does not support logical operations
		"""
		return self.data > rnode.data

if __name__ == '__main__':
	node1 = Node(1)
	node2 = Node(2)
	print(-node1)
	print(node1+node2)
	print(node1-node2)
	print(node1*node2)
	print(node1//node2)
	print(node1/node2)
	print(node1<node2)
	print(node1<=node2)
	print(node1==node2)
	print(node1!=node2)
	print(node1>=node2)
	print(node1>node2)