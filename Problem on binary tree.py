# Data-Structure-in-Python
***check children sum property  in a binary tree***
class Node:
  def __init__(self,data=None,left=None,right=None):
    self.data=data
    self.left=left
    self.right=right

def haschildrenSumproperty(root):
  if root is None:
    return 0
  if root.left is None and root.right is None:
    return root.data
  left=haschildrenSumproperty(root.left)
  right=haschildrenSumproperty(root.right)
  if root.data==left+right:
    return root.data

#if __name__=="__main__":
root=Node(25)
root.left=Node(12)
root.right=Node(13)
root.left.left=Node(7)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
if(haschildrenSumproperty(root))!=float("-inf"):
  print("Yes sum property have a children")
else:
  print("No sum property is no in children")
