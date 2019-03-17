# array element frequencies  
import collections
def freqCount(arr):
    return collections.Counter(arr)

if __name__=='__main__':

    arr=[2,3,5,4,6,2,5,7,8,1,5,4]
    freq=freqCount(arr)
    for key,value in freq.items():
        print(key,':',value)
print(freq)    
        
      