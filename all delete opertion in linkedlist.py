# Data-Structure-in-Python
***delete opertaion ***
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
    def delfirst(self):
        temp=self.head.next
        del self.head
        self.head=temp
    def dellast(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def delany(self,nodedata):
        temp=self.head
        while temp.next.data!=nodedata:
            temp=temp.next
        temp1=temp.next.next
        temp.next.next=None
        temp.next=temp1


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
print()
l.delany(3)
l.view()
