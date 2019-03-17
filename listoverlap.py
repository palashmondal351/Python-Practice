# LIST overlap, Find the common element in between the two list
l1=[1,5,3,9,7,5,2,8]
l2=[9,7,4,1,2,3,6]
def listoverlap(l1,l2):
    l=[each for each in l1 if each in l2]
    print(l)
listoverlap(l1,l2)