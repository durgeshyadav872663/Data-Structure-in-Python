**#LinkedList presentation**
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 

# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked List object 
    def __init__(self):  
        self.head = None

# lets create linked list with head alonge with three nodes     
llist = LinkedList() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
llist.head=first
first.next=second
second.next=third

**#Linked List Transversal**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None
    def displaynode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
llist.head=first
first.next=second
second.next=third
llist.displaynode()

**delete first node**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def deletefirstNode(self): #it is used for deleting first node
        if self.head==None:
            print("linked list empty")
        else:
            self.head=self.head.next

    def viewnode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
    
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
llist.head=first
first.next=second
second.next=third
llist.viewnode()
llist.deletefirstNode()
print()
llist.viewnode()

**delete last node**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def deletelastnode(self): #it is used for deleting last node
          temp=self.head
          while (temp.next.next)!= None:
              temp=temp.next
          temp.next=None

    def viewnode(self):# it is used for print linkedlist all elements
        temp=self.head
        while temp!=None:
            print(temp.data,end=(" ")) 
            temp=temp.next
    
llist = Linkedlist() 
first= Node(1) 
second = Node(2) 
third = Node(3) 
llist.head=first
first.next=second
second.next=third
llist.viewnode()
llist.deletelastnode()
print()
llist.viewnode()

**delete any node**
class Node: # used for creating node in linkedlist
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist: # used for linking all node and carrying head pointer(head)
    def __init__(self):
        self.head=None

    def deleteany(self,node): #it is used for deleting any node
          temp=self.head
          for i in range(2, node):
              temp=temp.next
          temp.next=temp.next.next

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
llist.deleteany(2)
print()
llist.viewnode()
