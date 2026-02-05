def factorial(n):
    #Base Case

    if n==0 or n==1:
        return 1
    #Recursion case
    else:
        return n*factorial(n-1)

#Testing the function

print(factorial(50))#Output:120
print(type(factorial(50)))
