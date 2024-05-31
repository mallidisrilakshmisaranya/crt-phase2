def enqueue(Q,ele):
    Q.append(ele)
    print(ele,"inserted into Queue")
def deQueue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    else:
        print(Q[0],"is getting deleted")
        Q.pop(0)
Q=()
enqueue(Q,10)
enqueue(Q,30)
enqueue(Q,40)
enqueue(Q,50)
print(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)












        












        












        











        













        











        
