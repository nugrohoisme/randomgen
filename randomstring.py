import random
import string

def randomString(length=10, type=1):
    if type == 1:
        chars = string.ascii_letters
    elif type == 2:
        chars = string.ascii_lowercase
    elif type == 3:
        chars = string.digits
    elif type == 4:
        chars = string.ascii_letters + string.digits
    elif type == 5:
        chars = string.ascii_lowercase + string.digits
    elif type == 6:
        chars = string.ascii_letters + string.digits + string.punctuation
    elif type == 7:
        chars = string.ascii_lowercase + string.digits + string.punctuation
        
    return ''.join((random.choice(chars) for i in range(length)))

if __name__ == '__main__':
    print ""
    print "#############################"
    print "#  RANDOM STRING GENERATOR  #"
    print "#############################"
    print ""    
    print "1. Letters"
    print "2. Letters (lowercase)"
    print "3. Digits"
    print "4. Alphanumeric"
    print "5. Alphanumeric (lowercase)"
    print "6. Alphanumeric with symbols"
    print "7. Alphanumeric (lowercase) with symbols"
    
    while True:        
        print "Choose type (1-7):",
        
        try:
            opt = int(input())
            
            if not (opt >= 1 and opt <= 7):
                raise Exception
            else:
                break
        except:
            print "Please insert proper answer..."
    
    while True:
        print "Insert length:",
        
        try:
            length = int(input())
            break
        except:
            print "Please insert proper answer..."
    
    print ""
    print 'Result:\n{}'.format(randomString(length, opt))
    print ""