**insertion node at first**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def insertfirst(self,value): #it is used for creating new node and adding at first 
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            self.head.next=temp
    def viewnode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
    
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
fourth=Node(4)
fifth=Node(5)
llist.head=first
first.next=second
second.next=third
third.next=fourth
fourth.next=fifth
llist.viewnode()
llist.insertfirst(8)
print()
llist.viewnode()


**insertion node at last**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def insertlast(self,value): #it is used for creating new node and adding at last 
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

    def viewnode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
    
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
fourth=Node(4)
fifth=Node(5)
llist.head=first
first.next=second
second.next=third
third.next=fourth
fourth.next=fifth
llist.viewnode()
llist.insertlast(8)
print()
llist.viewnode()

**inset node before any node**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def insertbefore(self,node,value): #it is used for creating new node and insert before any node
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            for i in range (2,node):
                temp=temp.next
            temp2=temp.next
            temp.next=newnode
            newnode.next=temp2
            
    def viewnode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
    
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
fourth=Node(4)
fifth=Node(5)
llist.head=first
first.next=second
second.next=third
third.next=fourth
fourth.next=fifth
llist.viewnode()
llist.insertbefore(2,8)
print()
llist.viewnode()
