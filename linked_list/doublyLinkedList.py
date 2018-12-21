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

        #Checking if argument is iterable or not
        try:
            iter(iterable)
        except TypeError:
            error.error_message("TypeError","__init__(): Argument passed is not an iterable. Empty DLL created")
            return

        for iterator in iterable:
            if isinstance(iterable,doublyLinkedList):
                iterator=iterator.data
            if self.length==0:
                self.head=Node.Node(iterator)
                self.end=self.head
            else:
                self.end.next=Node.Node(iterator)
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
            Converting DLL to a string
        """
        if self.head is None:
            return ""
        temp=self.head
        string=""
        while temp:
            string+=str(temp)
            temp=temp.next
        return string

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
    
    def __eq__(self,dll):
        """
            Compares doubly linked list with dll argument passed.
            Returns True if both the DLLs are equal, otherwise False.
        """
        if isinstance(dll,doublyLinkedList) is False:
            return False
        elif dll.length!=self.length:
            return False
        else:
            iter=self.head
            for i in dll:
                if i.data!=iter.data:
                    return False
                iter=iter.next
            return True

    def __ne__(self,dll):
        """
           Compares the doubly linked list with dll argument passed.
           Returns True if both the DLLs are not equal, otherwise False.  
        """
        return not self==dll

    def __len__(self):
        return self.length
    
    # def __min__(self):
    #     """
    #         Returns the minimum element of the DLL
    #     """
    #     iterobj=iter(self)
    #     min=next(iterobj).data
    #     while True:
    #         try:
    #             element=next(iterobj).data
    #         except StopIteration:
    #             break
    #         try:
    #             if element<min:
    #                 min=element
    #         except:
    #             error.error_message("TypeError","__min__(): Elements could not be compared")
    #     return min

    # def __max__(self):
    #     """
    #         Returns the maximum element of the DLL 
    #     """
    #     iterobj=iter(self)
    #     max=next(iterobj).data
    #     print(type(max))
    #     while True:
    #         try:
    #             element=next(iterobj)
    #         except StopIteration:
    #             break
    #         # try:
    #         #     if element.data>max:
    #         #         max=element.data
    #         # except TypeError:
    #         #     error.error_message("ValueError", "__max__(): elements of DLL could not be compared")

    #     return max
    
    def _insert_before_node(self,iter,node):
        if iter is None:
            if self.length==0:
                self.head=node
                self.end=self.head
                self.length=0
            else:
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
            self.length+=1
        else:
            index=min(index,self.length)
            index=index+self.length if index<0 else index
            index=max(0,index)
            node=Node.Node(ele)

            iter=self.head
            while index>0:
                iter=iter.next
                index-=1

            self._insert_before_node(iter,node)
        return
    
    def push(self,ele):
        """
            Adds element to the end of the DLL.
        """
        self.insert(ele,self.length)
        return
    
    def _remove_node(self,iter):
        if iter==self.head:
            if self.length==1:
                self.head=None
                self.end=None
                self.length=0
            else:
                self.head=self.head.next
                self.head.prev=None
                self.length-=1
        elif iter==self.end:
            self.end=self.end.prev
            self.end.next=None
            self.length-=1
        else:
            iter.next.prev=iter.prev
            iter.prev.next=iter.next
            self.length-=1
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
        self._remove_node(iter)
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

    def remove(self,ele):
        """
            Removes the first occurence of the element
        """
        try:
            if self.head is None:
                raise IndexError
            else:
                pass
        except IndexError:
            error.error_message("IndexError", "remove(ele): empty DLL")
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
                raise IndexError
            else:
                pass
        except IndexError:
            error.error_message("IndexError", "remove_last(ele): empty DLL")
        
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
            new_dll.push(i.data)
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
            if isinstance(iterable,doublyLinkedList):
                i=i.data
            self.push(i)
        return 

    def pop(self):
        """
            Deletes the last element in the DLL and returns it.
        """
        try:
            if self.length==0:
                raise IndexError
            else:
                pass
        except:
            error.error_message("IndexError","pop(): empty DLL")
        val=self.end.data
        self.delete(-1)
        return val

    def issorted(self):
        """
            Checks if a DLL is sorted or not.
            Returns True if it's sorted, otherwise False
        """
        if self.length==0:
            return True
        else:
            iterobj=iter(self)
            temp=next(iterobj).data
            while True:
                try:
                    temp_next=next(iterobj).data
                except StopIteration:
                    break
            
                if temp>temp_next:
                    return False
                temp=temp_next
            return True    


    def merge_sort(self,iterable):
        """ 
            If a sorted iterable is passed, then the values are added to the present DLL in such a way
            that resulting DLL is also sorted.
        """
        try:
            iter(iterable)
        except TypeError:
            error.error_message("TypeError","merge_sort(iterable): Argument passed is not an iterable")
            return

        #Checking if the argument is sorted
        new_dll=doublyLinkedList(iterable)
        try:        
            if new_dll.issorted() is False:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError","merge_sort(iterable): Iterable passed should be sorted")
            return

        #Checking if the DLL is sorted
        try:        
            if self.issorted() is False:
                raise ValueError
            else:
                pass
        except ValueError:
            error.error_message("ValueError","merge_sort(iterable): Self DLL is not sorted")
            return

        iterator=self.head
        while iterator and new_dll.length!=0:
            dll_data=new_dll.head.data
            iterdata=iterator.data
            if dll_data<iterdata:
                new_node=Node.Node(dll_data)
                self._insert_before_node(iterator,new_node)
                new_dll.delete(0)
            else:
                iterator=iterator.next
        if iterator is None and new_dll.length!=0:
            print(type(new_dll.head.data))
            self.extend(new_dll)
        return

    def insort(self,ele,sortCheck=True):
        """
            If DLL is sorted, insert ele such that it remains sorted. 
        """
        #Checking if the DLL is sorted
        if sortCheck:
            try:        
                if self.issorted() is False:
                    raise ValueError
                else:
                    pass
            except ValueError:
                error.error_message("ValueError","insort(ele): Self DLL is not sorted")
                return
        else:
            pass
        iterable=self.head
        while iterable:
            if iterable.data>ele:
                break
            iterable=iterable.next
        
        self._insert_before_node(iterable,Node.Node(ele))
        return

    def sort(self):
        """
            Insertion sorts the DLL.
        """
        if self.length==0:
            return
        else:
            pass
        new_dll=doublyLinkedList()
        iterator=self.head
        while iterator:
            new_dll.insort(iterator.data,False)
            iterator=iterator.next
        self.head=None
        self.end=None
        self.length=0
        self.extend(new_dll)
        return