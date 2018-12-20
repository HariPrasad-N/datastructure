class doublyLinkedList():
    def __init__(self):
        self.head=None
        self.end=None
        self.length=0

    def insert(self,ele,index=0):
        if not self.head:
            self.head=Node(ele)