import Node

class SinglyLinkedList:
	head=None
	def __init__(self,iterable):
		node=None
		prev=None
		for ele in iterable:
			node= Node.Node(ele)
			if prev:
				prev.next=node
			else:
				self.head=node
			prev=node
	
	def __str__(self):
		if self.head==None:
			return "None"
		temp=self.head
		string=""
		while temp:
			string+=str(temp.data)+" -> "
			temp=temp.next
		return string

	def __repr__(self):
		if self.head==None:
			return "None"
		temp=self.head
		string=""
		while temp:
			string+=str(temp.data)+" -> "
			temp=temp.next
		return string

if __name__ == '__main__':
	sll = SinglyLinkedList([1,2,3,4,5])
	print(sll)


