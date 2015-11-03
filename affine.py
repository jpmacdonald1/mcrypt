#Used for default settings
import random

def encrypt(plaintext,a=None,b=None):
    if a==None or b == None:
        print 'Some arguments missing. Selecting random...' 
    if a==None: 
        a=random.choice([1,3,5,7,11,13,17,19,23])
        print 'Using a= '+str(a)
    if b==None: 
        b=random.choice(range(1,25))
        print 'Using b= ' + str(b)
    return ''.join([chr( ( (a * ord(x) - 65 + b) % 26) + 65) for x in plaintext.upper() if x.isalpha()])
