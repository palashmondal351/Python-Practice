# Leap year checking 
def leapyear(year):
    if (year%400==0 and year%4==0):
        print(year,'is a leap year')
    elif (year%400!=0 and year%4==0):
        print(year,'is not a leap year')
    else:
        print(year,'is not a leap year')

year=int(input('Enter a year:'))        
leapyear(year)
