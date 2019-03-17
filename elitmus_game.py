# Take multiple input from user 
#print(list(map(int,input('Give input with sapace:').split())))
import sys
print('Total no of coin is 11')
c=11
p1=input('Write your name here:')
p2=input('Write opponent name here:')
print('\nHi',p1,'and',p2,'you can choose maximum of 5 coin')


######## FIRST CHOICE############
print('\n********First choice**********')
print('\nHi',p1,'you will choose first')
fc=int(input('Choose coin:'))
c-=fc
print(p1,'choose',fc,'coin and remaning coin is:',c)

print('\nHi',p2,'you will choose second')
sc=int(input('Choose coin:'))
c-=sc
print('\n=====First Choice Summery======')
print(p1,'choose',fc,'coin and',p2,'choose',sc, 'remaning coin is:',c)
################# SECOND CHOICE################ 
print('\n********Second choice**********')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
   
if c==1:
    print(p1,'lost the game')
    sys.exit
else:   
    print('\nHi',p1,'you will choose next')
    tc=int(input('Choose coin:'))
    c-=tc
    print(p1,'choose',(fc+tc),'coin and',p2,'choose',(sc), 'coin is:',c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    if c==1:
        print(p2,'lost the game')
        sys.exit
    else:
        print('\nHi',p2,'you will choose next')
        foc=int(input('Choose coin:'))
        c-=foc
        print('\n=====second Choice Summery======')
        print(p1,'choose',(fc+tc),'coin and',p2,'choose',(sc+foc), 'coin is:',c) 
        
################ THIRD CHOICE #################
        print('\n*******Third choice**********')
        if c==1:
            print(p1,'lost the game')
            sys.exit
        else:
            print('\nHi',p1,'you will choose next')
            fvc=int(input('Choose coin:'))
            c-=fvc
            print(p1,'choose',(fc+tc+fvc),'coin and',p2,'choose',(sc+foc), 'remaning coin is:',c)

            if c==1:
                print(p2,'lost the game')
                sys.exit
            else:
                print('\nHi',p2,'you will choose next')
                sic=int(input('Choose coin:'))
                c-=sic
                print('\n=====Third Choice Summery======')
                print(p1,'choose',(fc+tc+fvc),'coin and',p2,'choose',(sc+fc+sic), 'remaning coin is:',c)    