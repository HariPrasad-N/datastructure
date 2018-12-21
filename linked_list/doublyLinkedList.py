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
        """
            returns self for calling next in order to iterate through dll.
        """
        self.iter=self.head
        return self
    
    def __next__(self):
        """
            defines the function next for iterating
        """
        if self.iter is None:
            raise StopIteration
        val=self.iter
        self.iter=self.iter.next
        return val

    def __str__(self):
        """
            Allowing to convert doubly_linked_list to a string
        """
        if not self.head:
            return "None"
        temp=self.head
        string=""
        while temp:
            string+=str(temp.data)+" -><- "
            temp=temp.next
        return string

    def __repr__(self):
        """
            Changes the representation of the dll to a more readable form.
        """
        if self.head==None:
            return "None"
        temp=self.head
        string=""
        while temp:
            string+=str(temp.data)+" -><- "
            temp=temp.next
        return string
    
    def insert(self,ele,index=0):
        """
            Inserts ele at specified index. Float value of index will be floored. 
            If index is not specified, inserts at the head. Indexing starts from 0.
            Returns NoneType
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
        return
    
    def delete(self,index):
        """
            Deletes element at index passed as an argument. Index must not exceed the length limits.
            returns NoneType
        """
        try:
            index=int(index)
            if index>=self.length or index<self.length*-1:
                raise IndexError
        except ValueError:
            print("TypeError: index must be int or float")
            return
        except IndexError:
            print("IndexError: index must be within [-len,len)")
            return
        
        index= index+self.length if index<0 else index
        iter=self.head
        while index>0:
            iter=iter.next
            index-=1

        if iter==self.head:
            self.head=self.head.next
            self.head.prev=None
        elif iter==self.end:
            self.end=self.end.prev
            self.end.next=None
        else:
            iter.next.prev=iter.prev
            iter.prev.next=iter.next
        self.length-=1
        return
        
    def find(self,ele):
        """
            Checks if an element, passed as an argument is present in the dll. 
            Returns the first occuring index of the element if found, -1 if the element is not present.
        """
        self.end.next=Node.Node(ele)
        iter=self.head
        index=0
        while iter.data!=ele:
            iter=iter.next
            index+=1
        
        self.end.next=None
        if index==self.length:
            return -1
        else:
            return index

    def find_rev(self,ele):
        """
            Checks if an element, passed as an argument is present in the dll. 
            Returns the last occuring index of the element if found, -1 if the element is not present.
        """
        self.head.prev=Node.Node(ele)
        iter=self.end
        index=self.length-1
        while iter.data!=ele:
            iter=iter.prev
            index-=1
        
        self.head.prev=None
        return index
    
    def find_all(self,ele):
        """
            Checks all the occurences of element ele. 
            Returns a list of all the indices, empty list if the element is not present.
        """
        indices=[]
        iter=self.head
        for i in range(self.length):
            if iter.data==ele:
                indices.append(i)
            iter=iter.next
        return indices