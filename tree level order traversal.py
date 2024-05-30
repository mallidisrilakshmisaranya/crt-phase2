def printLevelOrderTraversal(root):
    if root==None:
        return
    Q=[root]
    result=[]
    while len(Q):
        subResult=[]
        for i in range(n):
            #step-1:deleting
            currNode=Q.pop(0)
            #step-2:appending to subresult
            subResult.append(currNode.data)
            #step3:enquing the left child
            if currNode.left!=None:
                Q.append(currNode.left)
            #step4:enquing the right child
            if currNode.right!=None:
                 Q.append(currNode.right)
        result.append(subResult)
    print(result)
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


printLevelOrderTraversal(obj1)
print()     
     
        
        
