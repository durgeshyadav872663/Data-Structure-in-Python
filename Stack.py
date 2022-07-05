# Data-Structure-in-Python
#***stack***
#using list
class Stack:
  def __init__(self,size):
    self.items=[]
    self.size=size
  def push(self,data):
    if self.size == len(self.items): #if size of linkist equal to length of of self.items then stack is full
      print(" Stack is full")
    else:
      self.items.append(data)    #append the data 
  def pop(self):
    if self.items==[]:
      print("Stack is empty")
    else:
      self.items.pop()
  def view(self):
    print(self.items)

s=Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
#s.pop()
s.view()
s.pop()
s.view()

#using queue
import queue
stack=queue.LifoQueue(maxsize=5)
print(stack.qsize())
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.queue)
print(stack.full())
stack.get()
print(stack.queue)
stack.put(5)
stack.put(6)
print(stack.queue)
stack.put(7)
print(stack.queue)
stack.get()
stack.get()
stack.get()
stack.get()
stack.get_nowait()

***using collections deque***
from collections import deque

stack1 =deque()
stack1.append(1)
stack1.append(2)
stack1.append(3)
print(stack1)
stack1.pop()
print(stack1)
stack1.insert(0,6)
print(stack1)
stack1.extend([2,3,4])
print(stack1)
stack1.remove(2)
print(stack1)
stack1.reverse()
print(stack1)
