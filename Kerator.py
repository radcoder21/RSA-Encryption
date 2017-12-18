def Cprime(turn):
    x = 0
    if turn == 'lock':
        x = eval(input("\nEnter your %s number, try and make it as small as possible: "%(turn)))
        return x
    else:
        while not isPrime(x):
            try:
                x = eval(input("\nEnter your %s prime number: " % (turn)))
                if isPrime(x):
                    return x
                else:
                    print("\nPlease enter a valid number...")
            except:
                print("\nPlease enter a valid number...")
    


def inputs():
        print("\nPlease enter two different prime numbers whose multiple will create\na limit that will determine the number range\nof your own personalized RSA encryption/decryption lock and key system.")
        p = Cprime('first')
        q = Cprime('second')
        print('\nYour limit is:',p*q)
        n,e,m = locknkey(p,q)
        return n,e,m
            
def gcd(n,e):
    while e != 0:
        final = n%e
        n = e
        e = final
    return n
    

def isPrime(x):
    num = 2
    prime = True
    if x < 2:
        prime = False
    while num < x and prime == True:
        if x % num == 0:
            prime = False
        num += 1
    return prime
        
def locknkey(p,q):
    n = p*q
    m = (p-1)*(q-1)
    print("\nEnter another prime for your lock, make it as small as possible...\nThis prime should be relatively prime\nto the multiple of the first two prime:",m)
    e = Cprime('lock')
    while gcd(m,e)!=1 or e<2:
        try:
            print("\nEnter another prime for your lock, make it as small as possible...\nThis prime should be relatively prime\nto the multiple of the first two prime:",m)
            e = Cprime('lock')
        except:
            print("\nInvalid input, please try again")
    print("\nYour lock is:",e)
    return n,e,m

def keyCreate(phi,lock):
    i = 1
    num = 0
    while num != 1:
        key = ((i*phi+1)/lock)
        if key == int(key) and key!=lock:
            num = (lock*int(key))%phi
        i += 1
    print("\nYour key is:",key)
    return int(key)


def main():
    n,e,m = inputs()
    d = keyCreate(m,e)
    #x=249
    #new = x**e%n
    #nex = new**d%n
    #print(x,new,nex,d)
    print("\nYour limit and public key are (%d,%d)"%(n,e))
    print("\nYour limit and private key are (%d,%d)"%(n,d))
    

main()

