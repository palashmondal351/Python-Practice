# Rock paper game.
# Rule: Rock beats scissors, Scissors beats paper, Paper beats rock
import sys
u11=input('What is your name?')
u22=input('What is your name?')
cu1=input('%s What you want to choose as name ROCK or SCISSORS or PAPER:'%u11)
cu2=input('%s What you want to choose as name ROCK or SCISSORS or PAPER:'%u22)
def Rockpaper(u1,u2):
    if (u1==u2):
        print('tie')
    elif u1=='ROCK':
        if u2=='SCISSORS':
            return ('\nROCK win')
        else:
            return ('\nPAPER win')
    elif u1=='SCISSORS':
        if u2=='PAPER':
            return ('\nSCISSORS win')
        else:
            return ('\nROCK win')
    elif u1=='PAPER':
        if u2=='ROCK':
            return ('\nPAPER win')
        else:
            return('\nSCISSORS win')
    else:
        return('Given choice is invalid!!!')
        sys.exit()
        
print(Rockpaper(cu1,cu2))
print('\nRule: Rock beats scissors, Scissors beats paper, Paper beats rock')        
            