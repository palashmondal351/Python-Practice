shopping={'Rice':100, 'Fish': 75, 'Veg':50, 'DNeeds':87, 'Others':45}


name=input('What is your father name:')
money=int(input('How much money initially have:'))

print('\nHere it is the market report')
print('...............')
print('\n')

print('\nMr./Ms.',name,'went market with initially',money,'money')
print('\nTotal Purchase items:',len(shopping))

k=shopping.keys()
m=shopping.values()
k=list(k)
print('\nPurchase items are',k)
m=list(m)
print('\nPurchase items prices',m )
print('\nTotal Cost:',sum(m))
print('\nRemaning Money:',money-sum(m))
