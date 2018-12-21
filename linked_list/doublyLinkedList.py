from utils import Node
from utils import error
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
        if self.head is None:
            return "None"
        temp=self.head
        string="{ "
        while temp!=self.end:
            string+=str(temp)+" -><- "
            temp=temp.next
        string+=str(temp)
        return string+" }"

    def __repr__(self):
        """
            Changes the representation of the dll to a more readable form.
        """
        if self.head==None:
            return "None"
        temp=self.head
        string="{ "
        while temp!=self.end:
            string+=str(temp)+" -><- "
            temp=temp.next
        string+=str(temp)
        return string+" }"
    
    def insert(self,ele,index=0):
        """
            Inserts ele at specified index. Float value of index will be floored. 
            If index is not specified, inserts at the head. Indexing starts from 0.
            Returns NoneType
        """
        try:
            index=int(index)
        except ValueError:
            error.error_message("ValueError", "insert(ele,index): Index should be of type int or float")
            return 
            

        if self.head is None:
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
    
    def push(self,ele):
        """
            Adds element to the end of the DLL.
        """
        self.insert(ele,self.length)
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
            error.error_message("ValueError", "delete(index): index must be int or float")
            return
        except IndexError:
            error.error_message("IndexError", "delete(index): index must be within [-len,len)")
            return
        
        index= index+self.length if index<0 else index
        iter=self.head
        while index>0:
            iter=iter.next
            index-=1

        if iter==self.head:
            if self.length==1:
                self.head=None
                self.end=None
                self.length=0
            else:
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
        if self.head is None:
            return -1

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

    def find_last(self,ele):
        """
            Checks if an element, passed as an argument is present in the dll. 
            Returns the last occuring index of the element if found, -1 if the element is not present.
        """
        if self.head is None:
            return -1
        
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
    
    def _remove_node(self,iter):
        if iter==self.head:
            if self.length==1:
                self.head=None
                self.end=None
                self.length=0
            else:
                self.head=self.head.next
                self.head.prev=None
        elif iter==self.end:
            self.end=self.end.prev
            self.end.next=None
        else:
            iter.next.prev=iter.prev
            iter.prev.next=iter.next
        self.length-=1

    def remove(self,ele):
        """
            Removes the first occurence of the element
        """
        try:
            if self.head is None:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError", "remove(ele): empty DLL")
            return
        
        self.end.next=Node.Node(ele)
        iter=self.head
        while iter.data!=ele:
            iter=iter.next

        try:
            if self.end.next==iter:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError", "remove(ele): Element not found in the DLL")
            self.end.next=None
            return

        self.end.next=None
        self._remove_node(iter)
        return
    
    def remove_last(self,ele):
        """
            Removes the last occurence of element.
        """
        try:
            if self.length==0:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError", "remove_last(ele): empty DLL")
        
        iter=self.end
        self.head.prev=Node.Node(ele)
        while iter.data!=ele:
            iter=iter.prev
        try:
            if iter==self.head.prev:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError","remove_last(ele): Element not found in the DLL")
            self.head.prev=None
            return
        self.head.prev=None
        self._remove_node(iter)
        return

    def remove_all(self,ele):
        """
            Removes all the occurences of Element.
        """
        try:
            if self.length==0:
                raise ValueError
        except ValueError:
            error.error_message("ValueError","remove_all(ele): empty DLL")
        
        presentFlag=False
        iter=self.head
        for i in range(self.length):
            if iter.data==ele:
                self._remove_node(iter)
                presentFlag=True
            iter=iter.next
        
        try:
            if presentFlag is False:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError","remove_all(ele): Element not found in the DLL")
        return 

    def __add__(self,dll):
        """
            Addition of two dll gives an concatenated dll. Returns a dll.
        """
        try:
            if isinstance(dll,doublyLinkedList) is False:
                raise TypeError
            else:
                pass
        except:
            error.error_message("TypeError","__add__(dll): cannot concatenate "+ str(type(dll))+ " to a DLL")
            return

        new_dll=doublyLinkedList(self)
        for i in dll:
            new_dll.push(i)
        return new_dll

    def append(self,ele):
        """
            Appends the element passed as an argument and updates the current DLL. 
            Returns NoneType
        """
        self.push(ele)
        return
    
    def extend(self,iterable):
        """
            Extends the iterable's elements to the DLL.
            Iterable need not be a DLL.
            Returns NoneType
        """
        try:
            iter(iterable)
        except TypeError:
            error.error_message("TypeError","Argument passed is not an iterable")
            return
        for i in iterable:
            self.push(i)
        return 
