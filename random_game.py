# random no game

string=str(input('Enter your name here:'))
k=sum(map(ord, string))
print('\nSummation of ASCII values of your name:',k)

q=[int(x) for x in str(k)]
print(sum(q))