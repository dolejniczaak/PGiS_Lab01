def funkcja(lista):
    for x in lista:
        if x%15==0:
            print "Fizz Buzz"
        elif x % 3 == 0:
            print "Fizz"
        elif  x%5==0:
            print "Buzz" 
        else:
            print x
cyfry=xrange(1,101)
ciag=funkcja(cyfry)