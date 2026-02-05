def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

# create the fibonacci generator
fib=fibonacci(15)

#Iterate and print the fibonacci Number

for num in fib:
    #print(num, end=",")
    print(num)
    
