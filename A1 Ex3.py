def fibonacci(n):
    for x in range( 0, n):
        if x == 0:
            y = 0
            print ("fib(" + str(x)+") =", y)
            y2 = y
        elif x == 1:
            y += 1
            print ("fib(" + str(x)+") =", y)
            y1 = y
        else:
            print ("fib(" + str(x)+") =", y)
            y2 = y1
            y1 = y
            y = y1 + y2            

fibonacci(20)
        
        
