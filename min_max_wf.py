# sorting withous using any optimization function
num = list(map(int, input("Enter a multiple value with space: ").split())) 
def minmaxsum(lis):
    i=1
    min=max=sum=lis[0]
    while i<len(lis):
        if lis[i]>max:
            max=lis[i]
        if lis[i]<min:
            min=lis[i]
        sum+=lis[i]
        i+=1
    return min, max, sum
min,max,sum=minmaxsum(num)
print('Given list is:', num)
print('Minimum is:',min,'\nMaximum is:',max,'\nSum:',sum, end='')
        
            