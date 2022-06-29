# Data-Structure-in-Python
***All Insert Operation***
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Linkedlist:
    def __init__(self):
        self.head=None 
    
    def view(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    

    def insertfirst(self,node):
        node.next=self.head
        self.head=node
    def insertlast(self,node):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node
    def insertany(self,oldnodedata,newnode):
        temp=self.head
        while temp.data!=oldnodedata:
            temp=temp.next
        temp1=temp.next
        temp.next=newnode
        newnode.next=temp1

        

first=Node(1)
second=Node(2)
third=Node(3)
fourth=Node(4)
l=Linkedlist()
l.head=first
first.next=second
second.next=third
third.next=fourth
l.view()
l.insertany(3,Node(8))
print()
l.view()
