# String Palindrom
string=str(input('Enter a string here:'))
if string[::]==string[::-1]:
    print('palindrom')
else:
    print('String is not palindrom')