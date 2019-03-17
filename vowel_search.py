#dheck vowel inside a word

def vol(string, vowel):
    l=[each for each in string if each in vowel]
    print('no of vouwl that found in',string,'is:',len(l))
    print(l)
    
string='Neural Network'
vowel='aeiouAEIOU'    
vol(string,vowel)