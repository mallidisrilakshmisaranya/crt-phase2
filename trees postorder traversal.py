class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printPostorder(root):
    if root==None:
        return
    #1
    printPostorder(root.left)
    #2
    printPostorder(root.right)
    #3
    print(root.data,end=", ")
obj1=node(12)
obj2=node(5)
obj3=node(8)
obj4=node(-1)
obj5=node(2)
obj6=node(89)

#creating links
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.right=obj6 


printPostorder(obj1)
print() 
