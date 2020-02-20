def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True

def twoDigits(n):
    if n<10:
        return False
    else:
        return True

def oneAndSeven(n):
    if(n%10 == 1 or n%10 == 7):
        return False
    if( n < 100):
        n = n//10
        if(n%10 == 1 or n%10 == 7):
            return False
    else:
        n = n//10
        if(n%10 == 1 or n%10 == 7):
            return False
        n = n//10
        if(n%10 == 1 or n%10 == 7):
            return False
    return True;

def tenSum(n):
    if (sum([ int(j) for j in str(n) ]) <= 10):
        return True;
    else:
        return False;

def equalDigits(n):
    tot = 0
    m = n
    if m == 0 :
        tot= 1
    else:
        while m > 0:
            m = m//10;
            tot += 1
    n=n%10
    if(tot == int(n)):
        return True;
    else:
        return False

def beforeLast(n):
    return 0

def twoFirsts(n):
    if( n > 99):
        while n > 99:
            n = n//10;
    n = (n//10) + (n%10)
    if (n%2 == 0):
        return False
    return True
    



i=1
while i < 1000:
    if ( isPrime(i) == True ):
        if ( twoDigits(i) == True):      
            if( oneAndSeven(i) == True ):
                if( tenSum(i) == True ):
                    if( equalDigits(i) == True):
                        if( twoFirsts(i) == True):
                            print(i)
                            i=i+1
                        else:
                             i=i+1   
                    else:
                        i=i+1
                else:
                    i=i+1
            else:
                i=i+1            
        else:
            i=i+1
    else:
        i=i+1


mystery_number = i

print(f'Le nombre mystère est le : {mystery_number}')
