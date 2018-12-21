from utils import Node
class doublyLinkedList():
    def __init__(self,iterable=[]):
        """
            attributes:
                length--> length of the doubly linked list
                head--> starting node of the doubly linked list
        """
        self.head=None
        self.end=None
        self.length=0
        self.iter=None

        for iter in iterable:
            if self.length==0:
                self.head=Node.Node(iter)
                self.end=self.head
            else:
                self.end.next=Node.Node(iter)
                self.end.next.prev=self.end
                self.end=self.end.next
            self.length+=1

    def __iter__(self):
        self.iter=self.head
        return self
    
    def __next__(self):
        if self.iter is None:
            raise StopIteration
        val=self.iter.data
        self.iter=self.iter.next
        return val

    def __str__(self):
        if not self.head:
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
    
    def insert(self,ele,index=0):
        """
            Inserts ele at specified index. Float value of index will be floored. 
            If index is not specified, inserts at the head. Indexing starts from 0.
        """
        try:
            index=int(index)
        except ValueError:
            print("TypeError: Index should be of type int or float")
            return 
            

        if not self.head:
            self.head=Node.Node(ele)
            self.end=self.head
        else:
            index=min(index,self.length)
            index=index+self.length if index<0 else index
            index=max(0,index)
            node=Node.Node(ele)

            iter=self.head
            while index>0:
                iter=iter.next
                index-=1

            if iter is None:
                node.prev=self.end
                self.end.next=node
                self.end=node
            elif iter==self.head:
                node.next=self.head
                self.head.prev=node
                self.head=node
            else:
                iter.prev.next=node
                node.next=iter
                node.prev=iter.prev
                iter.prev=node
        self.length+=1
