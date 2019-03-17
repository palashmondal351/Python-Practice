# find the largest string in a sentense and find the indices

n=list(map(str,input('Enter string here: ').split()))
q=[]
for i in n:
    m=len(i)
    q.append(m)
ind=q.index(max(q))
print('\nMaximum length string is:',n[ind],'\nwhich length is',max(q),'at index',ind)