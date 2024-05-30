class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printInorder(root):
    if root==None:
        return
    #1
    printInorder(root.left)
    #2
    print(root.data,end=", ")
    #3
    printInorder(root.right)
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


printInorder(obj1)
print()
